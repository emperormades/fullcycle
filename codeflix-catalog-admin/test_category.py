import unittest
from uuid import UUID
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

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="test")
        self.assertIsInstance(category.id, UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="test")
        self.assertEquals(category.name, "test")
        self.assertEquals(category.description, "")
        self.assertEquals(category.is_active, True)

if __name__ == "__main__":
    unittest.main()