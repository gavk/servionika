#!/usr/bin/env python

import unittest
import sys

sys.path.append("task-1.1")
from storage import *


class TestAddData(unittest.TestCase):
    def test_add_data_to_empty_storage(self):
        storage = get_new_storage()
        added_key = 'key'
        added_value = 'value'
        add_data(storage, added_key, added_value)
        values = get_data(storage, added_key)
        self.assertEqual(len(values), 1)
        self.assertIn(added_value, values)

    def test_add_data_to_existing_key(self):
        existing_key = 'key'
        existing_value = 'first_value'
        nonexisting_value = 'second_value'
        storage = get_new_storage()
        add_data(storage, existing_key, existing_value)
        add_data(storage, existing_key, nonexisting_value)
        values = get_data(storage, existing_key)
        self.assertIn(existing_value, values)
        self.assertIn(nonexisting_value, values)

    def test_get_data_from_nonexisting_key(self):
        nonexisting_key = 'second'
        storage = get_new_storage()
        values = get_data(storage, nonexisting_key)
        self.assertEqual(values, None)


if '__main__' == __name__:
    unittest.main()
