from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'account', AccountViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
