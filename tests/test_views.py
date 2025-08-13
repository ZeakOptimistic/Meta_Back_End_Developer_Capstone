from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=50, inventory=200)
        Menu.objects.create(title="Burger", price=40, inventory=150)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_data = MenuSerializer(items, many=True)
        self.assertEqual(len(serialized_data.data), 3)
        self.assertEqual(serialized_data.data[0]['title'], "IceCream")
