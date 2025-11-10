from django.shortcuts import render
from rest_framework import viewsets
from .models import Invoice, Quotation, InvoiceItem,QuotationItem,Payments
from .serializers import InvoiceSerializer, QuotationSerializer,QuotationItemSerializer, InvoiceItemSerializer,PaymentSerializer

# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
class QuotationItemViewSet(viewsets.ModelViewSet):
    queryset = QuotationItem.objects.all()
    serializer_class = QuotationItemSerializer
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer