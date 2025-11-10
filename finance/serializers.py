from rest_framework import serializers
from .models import Invoice, Quotation, InvoiceItem,QuotationItem,Payments


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
class QuotationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Quotation
        fields = '__all__'
class QuotationItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = QuotationItem
        fields = '__all__'
class PaymentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Payments
        fields = '__all__'