from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.InvoiceViewSet.as_view({'post': 'create'}), name='invoices'),
    # Define other URL patterns here
]
