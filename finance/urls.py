from rest_framework import routers
from .views import InvoiceViewSet, QuotationViewSet,InvoiceItemViewSet, QuotationItemViewSet,PaymentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceItemViewSet, QuotationViewSet, QuotationItemViewSet, PaymentViewSet

router = routers.DefaultRouter()
router.register(r'/invoice', InvoiceViewSet)
router.register(r'/invoice-item', InvoiceItemViewSet)
router.register(r'/quote', QuotationViewSet)
router.register(r'/quote-item', QuotationItemViewSet)
router.register(r'/payments', PaymentViewSet)
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoice-items', InvoiceItemViewSet)
router.register(r'quotations', QuotationViewSet)
router.register(r'quotation-items', QuotationItemViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = router.urls
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
