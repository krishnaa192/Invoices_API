from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            "date": "2023-08-07",
            "invoice_no": "INV123",
            "customer_name": "John Doe",
            "details": [
                {
                    "description": "Product A",
                    "quantity": 2,
                    "unit_price": 10.0,
                    "price": 20.0
                },
                {
                    "description": "Product B",
                    "quantity": 3,
                    "unit_price": 15.0,
                    "price": 45.0
                }
            ]
        }

    def test_create_invoice(self):
        response = self.client.post('/api/invoices/', data=self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(InvoiceDetail.objects.count(), 2)

    # Add more test methods for other endpoints (e.g., list, retrieve, update, delete)

# Add more test cases if needed
