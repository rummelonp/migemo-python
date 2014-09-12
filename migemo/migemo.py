import cffi
import os
import re
import sys

class Migemo:
    def __init__(self, dict_path):
        self.dict_path = dict_path
        self._ffi = self.__setup_ffi()
        self._lib = self.__load_lib(self._ffi)
        self._migemo_struct = self.__load_migemo(self._lib, self.dict_path)
        if not os.path.exists(dict_path):
            raise IOError("No such file: '%s'" % dict_path)

    def query(self, query):
        if not isinstance(query, str):
            query = query.encode()
        re_ptr = self._lib.migemo_query(self._migemo_struct, query)
        re_str = self._ffi.string(re_ptr)
        self._lib.migemo_release(self._migemo_struct, re_ptr)
        return re_str

    def __setup_ffi(self):
        ffi = cffi.FFI()
        ffi.cdef('''
typedef struct _migemo migemo;
migemo* migemo_open(const char* dict);
void migemo_release(migemo* object, unsigned char* string);
void migemo_close(migemo* object);
unsigned char* migemo_query(migemo* object, const unsigned char* query);
''')
        return ffi

    def __load_lib(self, ffi):
        if re.search('darwin', sys.platform):
            suffix = 'dylib'
        else:
            suffix = 'so'
        return ffi.dlopen('libmigemo.' + suffix)

    def __load_migemo(self, lib, dict_path):
        return lib.migemo_open(dict_path)

    def __del__(self):
        if self._migemo_struct is not None:
            self._lib.migemo_close(self._migemo_struct)
