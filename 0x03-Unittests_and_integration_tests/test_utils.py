#!/usr/bin/env python3
"""
This module test the util class and functions using parameterize and mocking
"""
from utils import (access_nested_map, get_json, memoize)
from parameterized import parameterized
from typing import Dict
from unittest.mock import patch, Mock
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ Class for Testing Access Nested Map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test that a KeyError is raised for the respective inputs"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Tests the get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload", True}),
        ("http://holberton.io", {"payload", False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Test that utils.get_json returns the expected results"""
        config = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**config)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Class for Testing Memoize """

    def test_memoize(self):
        """
            Using memoize to optimize function call
        """

        class TestClass:
            """ Test class for wrapping with memoize """

            def a_method(self):
                """method to be mocked"""
                return 42

            @memoize
            def a_property(self):
                """Method to call method to be mocked"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            """Use patch.object to mock Testclass"""
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
