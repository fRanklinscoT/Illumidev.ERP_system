from rest_framework import routers
from .views import InvoiceViewSet, QuotationViewSet,InvoiceItemViewSet, QuotationItemViewSet,PaymentViewSet

router = routers.DefaultRouter()
router.register(r'/invoice', InvoiceViewSet)
router.register(r'/invoice-item', InvoiceItemViewSet)
router.register(r'/quote', QuotationViewSet)
router.register(r'/quote-item', QuotationItemViewSet)
router.register(r'/payments', PaymentViewSet)

urlpatterns = router.urls
