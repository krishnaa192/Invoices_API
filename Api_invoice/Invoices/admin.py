from django.contrib import admin

# Register your models here.
from .models import Invoice, InvoiceDetail

admin.site.register(Invoice)
admin.site.register(InvoiceDetail)