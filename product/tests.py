from django.test import TestCase
from .models import Product

class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            category='Test Category',
            price=10.99
        )

    """Test the creation of a Product instance"""
    def test_product_creation(self):
        
        self.assertIsInstance(self.product, Product)
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.category, 'Test Category')
        self.assertAlmostEqual(self.product.price, 10.99)

    """Test the string representation of a Product instance"""
    def test_product_string_representation(self):
        self.assertEqual(str(self.product), 'Test Product')

    """Test the attributes of a Product instance"""
    def test_product_attributes(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.category, 'Test Category')
        self.assertAlmostEqual(self.product.price, 10.99)

    """Test updating a Product instance"""
    def test_product_update(self):
        updated_price = 15.99
        self.product.price = updated_price
        self.product.save()
        self.product.refresh_from_db()
        self.assertAlmostEqual(self.product.price, updated_price)

    """Test deleting a Product instance"""
    def test_product_deletion(self):
        product_id = self.product.id
        self.product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product_id)
