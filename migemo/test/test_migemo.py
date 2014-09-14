# -*- coding: utf-8 -*-

import unittest
import migemo

class TestMigemo(unittest.TestCase):
    dict_dir = '/usr/local/Cellar/cmigemo/20110227/share/migemo/'

    def dict_path(self, encoding):
        return '%s/%s/migemo-dict'%(self.dict_dir, encoding)

    def test_migemo_init(self):
        migemo_utf8 = migemo.Migemo(self.dict_path('utf-8'))
        self.assertTrue(isinstance(migemo_utf8, migemo.Migemo))
        migemo_utf8 = migemo.Migemo(self.dict_path(u'utf-8'))
        self.assertTrue(isinstance(migemo_utf8, migemo.Migemo))
        self.assertRaises(IOError, migemo.Migemo, 'invaid-path')

    def test_migemo_encoding(self):
        migemo_utf8 = migemo.Migemo(self.dict_path('utf-8'))
        migemo_eucjp = migemo.Migemo(self.dict_path('euc-jp'))
        self.assertEqual('utf_8', migemo_utf8.encoding())
        self.assertEqual('euc_jp', migemo_eucjp.encoding())

    def test_migemo_query(self):
        migemo_utf8 = migemo.Migemo(self.dict_path('utf-8'))
        migemo_eucjp = migemo.Migemo(self.dict_path('euc-jp'))

        re_unicode = u'(ﾆｬ[ﾝﾉﾈﾇﾆﾅ]|ニャ[ンノネヌニナ]|にゃ[んのねぬにな]|ｎｙａｎ|nyan)'
        query_unicode = u'nyan'
        query_str = 'nyan'

        self.assertEqual(re_unicode, migemo_utf8.query(query_unicode))
        self.assertEqual(re_unicode, migemo_utf8.query(query_str))

        self.assertEqual(re_unicode, migemo_eucjp.query(query_unicode))
        self.assertEqual(re_unicode, migemo_eucjp.query(query_str))

if __name__ == '__main__':
    unittest.main()
