from django.test import TestCase
from restaurant.views import MenuItemsView
from rest_framework.test import RequestsClient

client = RequestsClient()


# Menu Items Test
class MenuItemsView(TestCase):
    def test_menu_response(self):
        client = RequestsClient()
        response = client.get("http://127.0.0.1:8000/restaurant/menu-items")
        assert response.status_code == 200

    def test_menu_item(self):
        client = RequestsClient()
        response = client.get("http://127.0.0.1:8000/restaurant/menu-items/1")
        self.assertEqual(
            response.data,
            {"id": 1, "title": "Pasta", "price": "10.00", "inventory": 15},
        )
