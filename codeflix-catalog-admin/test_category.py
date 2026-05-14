import unittest
from category import Category

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaises(TypeError) as ctx:
            Category()
        self.assertEqual(
            str(ctx.exception),
            "Category.__init__() missing 1 required positional argument: 'name'",
        )

    def test_name_must_have_less_than_256_characters(self):
        with self.assertRaises(ValueError) as ctx:
            Category(name="a" * 256)
        self.assertEqual(
            str(ctx.exception),
            "Name must be less than 256 characters",
        )

if __name__ == "__main__":
    unittest.main()