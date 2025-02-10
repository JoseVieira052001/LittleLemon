from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Menu.objects.create(
            title="Banana",
            price=2,
            inventory=8
        )
        Menu.objects.create(
            title="Arroz",
            price=2.5,
            inventory=10
        )

    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemsView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)