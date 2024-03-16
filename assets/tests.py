from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from .models import Company, Employee

class CRUDTestCase(TestCase):
    def setUp(self):
        # Create a company for testing
        self.company = Company.objects.create(name='Test Company')
        self.employee_data = {'employeeName': 'Test Employee', 'companyId': self.company.pk}  # Use the actual ID of the created company

    def test_company_CRUD(self):
        response = self.client.post(reverse('add_company'), {'companyName': 'Test Company'})
        self.assertRedirects(response, reverse('company_list'))  # Check if redirected to company list after creation
        self.assertEqual(Company.objects.count(), 2)  # Check if the company is created

    def test_employee_CRUD(self):
        response = self.client.post(reverse('add_employee'), self.employee_data)
        self.assertRedirects(response, reverse('employee_list'))  # Check if redirected to employee list after creation
        self.assertEqual(Employee.objects.count(), 1)  # Check if the employee is created
