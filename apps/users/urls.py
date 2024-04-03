from django.urls import path, include
from rest_framework import routers
from apps.users.views import *

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', LoginAPIView.as_view()),
    path('api/logout/', LogoutAPIView.as_view()),
    path('api/change-password/', ChangePasswordAPIView.as_view()),
]
