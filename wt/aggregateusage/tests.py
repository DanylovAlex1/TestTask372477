from django.urls import reverse,resolve
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient


class AggregateUsageTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_outoflimit(self):
        data={'limit': 100}
        response = self.client.get('/aggregatedusage/user-outoflimit/100/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_subscr_outoflimit(self):
        data={'limit': 100}
        response = self.client.get('/aggregatedusage/subscr-outoflimit/100/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscr_outoflimitByDate(self):
        response = self.client.get("/aggregatedusage/subscr-outoflimitbydate/100/01.01.2001/01.01.2022/data/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

