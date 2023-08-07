from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    # Use the InvoiceDetailSerializer for the 'details' field
    details = InvoiceDetailSerializer(many=True, write_only=True)  # Note 'write_only'

    class Meta:
        model = Invoice
        fields = '__all__'
    
    def create(self, validated_data):
        details_data = validated_data.pop('details')  # Extract details data
        
        # Create the main Invoice instance
        invoice = Invoice.objects.create(**validated_data)  # Create the invoice
        
        # Create associated InvoiceDetail instances
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)  # Create associated details
        
        return invoice
