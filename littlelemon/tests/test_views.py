from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="Pizza", price=12, inventory=50)
        Menu.objects.create(title="Burger", price=8, inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('menu'))

        menus = Menu.objects.all()

        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)
