from django.test import TestCase
from selenium import webdriver
from .models import *
from django.urls import reverse


# first testcase..................
class first(TestCase):
    def setup(self):
        pass

    # def test_equal(self):
    #     self.assertEqual(0, 1)

    def test_equals(self):
        self.assertEqual(1, 1)
    # ------------------------------
    # def test_product_category(self):
    #     categories =['abc', 'def']
    #     for category in categories:
    #         obj = Product.objects.create(
    #             product_name = category
    #         )
    #         self.assertEquals(category, obj.product_name)
    #     obj = Product.objects.all()
    #     self.assertEqual(obj.count(), 2)
