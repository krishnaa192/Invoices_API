from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer

#Invoice Viewset for CRUD operations
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
