import unittest

from pysett.settings import dict_updater


class TestDictUpdater(unittest.TestCase):

    def test_updating_empty_dict(self):
        result = dict_updater(source={'a':1}, dest={})
        self.assertDictEqual({'a':1}, result)

    def test_overriding_value(self):
        result = dict_updater(source={'a':1}, dest={'a':2})
        self.assertDictEqual({'a':1}, result)

    def test_appending_value(self):
        result = dict_updater(source={'a':1}, dest={'b':2})
        self.assertDictEqual({'a':1, 'b':2}, result)

    def test_nested_dict_appending(self):
        source = {'a':{'b':1}}
        dest = {'a':{'c':2}}
        result = dict_updater(source, dest)
        self.assertDictEqual({'a':{'b':1, 'c':2}}, result)

    def test_appending_dict(self):
        source = {'d':{'b':1}}
        dest = {'a':{'c':2}}
        result = dict_updater(source, dest)
        self.assertDictEqual({'a':{'c':2}, 'd':{'b':1}}, result)


