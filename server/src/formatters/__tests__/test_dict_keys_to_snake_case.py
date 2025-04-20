import unittest

from src.formatters.dict_keys_to_snake_case import dict_keys_to_snake_case


class TestDictKeysToSnakeCase(unittest.TestCase):
    def test_simple_dict(self):
        # Arrange
        d = {"FooBar": 42}

        # Act
        actual = dict_keys_to_snake_case(d)

        # Assert
        self.assertEqual(actual, {"foo_bar": 42})
        self.assertEqual(d, {"FooBar": 42})

    def test_advanced_dict(self):
        # Arrange
        d = {
            "KeyA": {
                "KeyB": 42,
                "KeyC": {"KeyD": 12, "KeyE": [1, "42", True, {"KeyF": 1}]},
            }
        }

        # Act
        actual = dict_keys_to_snake_case(d)

        # Assert
        self.assertEqual(
            actual,
            {
                "key_a": {
                    "key_b": 42,
                    "key_c": {"key_d": 12, "key_e": [1, "42", True, {"key_f": 1}]},
                }
            },
        )
        self.assertEqual(
            d,
            {
                "KeyA": {
                    "KeyB": 42,
                    "KeyC": {"KeyD": 12, "KeyE": [1, "42", True, {"KeyF": 1}]},
                }
            },
        )
