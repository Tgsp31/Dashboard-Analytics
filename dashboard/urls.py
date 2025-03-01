from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataPointViewSet
from django.urls import path, include
from .views import index

router = DefaultRouter()
router.register(r'data', DataPointViewSet)






urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
