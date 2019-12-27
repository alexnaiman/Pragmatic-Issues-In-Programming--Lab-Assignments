import unittest
import logging
import parser
from builder import JsonBuilder


class TestStringMethods(unittest.TestCase):
    def test_empty_object(self):
        self.assertEqual(JsonBuilder().build(), '{')

    def test_basic_object(self):
        self.assertEqual(JsonBuilder().start_object().
                         put("key", "value").
                         end_object().
                         build(), '{"key": "value"}')

    def test_nested_object(self):
        self.assertEqual(JsonBuilder().
                         start_object().
                         put("key", "value").
                         start_object("nestedObject").
                         put("key", "value").
                         end_object().
                         end_object().
                         build(), '{"key": "value", "nestedObject": {"key": "value"}}')

    def test_nested_object_x2(self):
        self.assertEqual(JsonBuilder().
                         start_object().
                         put("key", "value").
                         start_object("nestedObject").
                         start_object("nestedObject2").
                         put("key", "value").
                         end_object().
                         end_object().
                         end_object().
                         build(), '{"key": "value", "nestedObject": {"nestedObject2": {"key": "value"}}}')

    def test_empty_array(self):
        self.assertEqual(JsonBuilder().start_array().end_array().build(), "[")

    def test_basic_array(self):
        self.assertEqual(JsonBuilder().
                         start_array().
                         put(2).
                         end_array().
                         build(), "[2]")

    def test_array_with_object(self):
        self.assertEqual(JsonBuilder().
                         start_array().
                         start_object().
                         put("key", "value").
                         end_object().
                         end_array().
                         build(), '[{"key": "value"}]')

    def test_object_with_array(self):
        self.assertEqual(JsonBuilder().start_object().
                         start_array("key").
                         put(2).
                         end_array().
                         end_object().
                         build(), '{"key": [2]}')

    def test_object_with_array_with_nested_object(self):
        self.assertEqual(JsonBuilder().start_object().
                         start_array("key").
                         start_object().
                         put("key", "value").
                         end_object().
                         put(2).
                         end_array().
                         end_object().
                         build(), '{"key": [{"key": "value"}, 2]}')

    def test_array_with_nested_object(self):
        self.assertEqual(JsonBuilder().
                         start_array().
                         start_object().
                         start_array("key").
                         start_object().
                         put("key", "value").
                         end_object().
                         end_array().
                         end_object().
                         put(2).
                         end_array().
                         build(), '[{"key": [{"key": "value"}]}, 2]')


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
        level=logging.INFO
    )
    unittest.main()
