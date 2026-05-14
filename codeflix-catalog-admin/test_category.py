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

if __name__ == "__main__":
    unittest.main()