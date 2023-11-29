from django.urls import path, include
from .views import ProductView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', ProductView, 'product')

urlpatterns=[
    path('api/', include(router.urls))
]