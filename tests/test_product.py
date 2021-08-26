import unittest

from application.product import Product, ENABLED, DISABLED

class TestProduct(unittest.TestCase):

    def test_product_enable(self):
        product = Product(name="Hello", status=DISABLED, price=10)
        enable = product.enabled()
        self.assertEqual(enable, None)
        self.assertEqual(product.status, ENABLED)

        product = Product(name="Hello", status=DISABLED, price=0)
        with self.assertRaises(ValueError) as e:
            product.enabled()

        self.assertEqual(
            "The price must be greater than zero to enable the product",
            str(e.exception)
        )

    def test_product_disabled(self):
        product = Product(name="Hello", status=DISABLED, price=0)
        disabled = product.disabled()
        self.assertEqual(disabled, None)
        self.assertEqual(product.status, DISABLED)

        product = Product(name="Hello", status=DISABLED, price=10)
        with self.assertRaises(ValueError) as e:
            product.disabled()

        self.assertEqual(
            "The price must be zero in order to have the product disabled",
            str(e.exception)
        )

