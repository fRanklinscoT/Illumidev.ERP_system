from rest_framework import routers
from .views import ClientViewSet,CompanyViewSet,UserViewSet,RoleViewSet

router = routers.DefaultRouter()
router.register(r'/users',UserViewSet)
router.register(r'/client',ClientViewSet)
router.register(r'/company',CompanyViewSet)
router.register(r'/roles',RoleViewSet)

urlpatterns = router.urls