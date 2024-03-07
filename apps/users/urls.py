from django.urls import path, include
from rest_framework import routers
from apps.users import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet, basename='user')

urlpatterns = [
    path('all/', include(router.urls))
]
