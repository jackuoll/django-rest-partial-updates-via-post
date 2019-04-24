from django.conf.urls import url, include
from rest_framework import routers
from .views import XViewSet

router = routers.DefaultRouter()
router.register(r'users', XViewSet)

urlpatterns = [
    url(r'^x/', include(router.urls)),
]
