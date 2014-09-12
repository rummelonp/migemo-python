import cffi
import re
import sys

class Migemo:
    def __init__(self, dict_path):
        self.dict_path = dict_path
        self._ffi = None
        self._lib = None
        self._migemo = None

    def query(self, query):
        if self._ffi is None:
            self._ffi = self.__setup_ffi()
        if self._lib is None:
            self._lib = self.__load_lib(self._ffi)
        if self._migemo is None:
            self._migemo = self.__load_migemo(self._lib, self.dict_path)
        re_ptr = self._lib.migemo_query(self._migemo, query)
        re_str = self._ffi.string(re_ptr)
        self._lib.migemo_release(self._migemo, re_ptr)
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
        if self._migemo is not None:
            self._lib.migemo_close(self._migemo)
