import unittest

from application.product import Product, ENABLED, DISABLED

class TestProduct(unittest.TestCase):

    def test_product_enable(self):
        product = Product(name="Hello", status=DISABLED, price=10)
        enable = product.enabled()
        self.assertEqual(enable, None)
        self.assertEqual(product.status(), ENABLED)

        product = Product(name="Hello", status=DISABLED, price=0)
        with self.assertRaises(ValueError) as e:
            product.enabled()

        self.assertEqual(
            "The price must be greater than zero to enable the product",
            str(e.exception)
        )
