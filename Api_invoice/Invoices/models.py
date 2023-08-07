from django.db import models
# Create your models here.
from django.db import models


# Create your models here.
# Invoice model
class Invoice(models.Model):
    date = models.DateField(null=True)
    invoice_no = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100,default='None')
# Invoice detail model
class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
