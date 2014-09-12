import cffi
import os
import re
import sys

class Migemo:
    libsuffix = 'dylib' if re.search('darwin', sys.platform) else 'so'

    cvariable = '''
    typedef struct _migemo migemo;
    '''

    cfunction = '''
    migemo* migemo_open(const char* dict);
    void migemo_release(migemo* object, unsigned char* string);
    void migemo_close(migemo* object);
    unsigned char* migemo_query(migemo* object, const unsigned char* query);
    '''

    ffi = cffi.FFI()
    ffi.cdef(cvariable)
    ffi.cdef(cfunction)

    lib = ffi.dlopen('libmigemo.' + libsuffix)

    def __init__(self, dict_path):
        if not os.path.exists(dict_path):
            raise IOError("No such file: '%s'" % dict_path)
        self.dict_path = dict_path
        self.migemo_struct = self.lib.migemo_open(self.dict_path)

    def __del__(self):
        if hasattr(self, 'migemo_struct') and self.migemo_struct is not None:
            self.lib.migemo_close(self.migemo_struct)

    def query(self, query):
        if not isinstance(query, str):
            query = query.encode()
        re_ptr = self.lib.migemo_query(self.migemo_struct, query)
        re_str = self.ffi.string(re_ptr)
        self.lib.migemo_release(self.migemo_struct, re_ptr)
        return re_str
