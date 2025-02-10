from django.test import TestCase
from restaurant.views import *
#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="IceCream",
            price=80,
            inventory=100
        )
        self.assertEqual(item.__str__(), "IceCream : 80")