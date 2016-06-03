# -*- coding: utf-8 -*-

import unittest
import script

test_list = [456,123,987,543]

test_list1 = [456,123,987,543]

expected_min_value = 123
expected_max_value = 987

expected_sorted_asc = [123,456,543,987]
expected_sorted_desc = [987,543,456,123]

class MinMaxSort(unittest.TestCase):
    
    def test_min_value(self):
        self.assertEqual(script.get_min_value(test_list), expected_min_value)

    def test_max_value(self):
        self.assertEqual(script.get_max_value(test_list), expected_max_value)

    def test_sort_asc(self):
        self.assertEqual(script.sort_asc(test_list), expected_sorted_asc)
    
    def test_sort_desc(self):
        self.assertEqual(script.sort_desc(test_list1), expected_sorted_desc)


if __name__ == '__main__':
    unittest.main()
