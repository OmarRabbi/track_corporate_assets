from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company, Employee

class CRUDTestCase(APITestCase):
    def setUp(self):
        self.company_data = {'name': 'Test Company'}
        self.employee_data = {'name': 'Test Employee', 'company': None}

    def test_company_CRUD(self):
        # Test creating a new company
        response = self.client.post(reverse('add-company'), self.company_data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)  # Redirect after creating

    def test_employee_CRUD(self):
        # Test creating a new employee
        response = self.client.post(reverse('add-employee'), self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)  # Redirect after creating
