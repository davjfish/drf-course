from django.urls import path, include
from . import views


# THIS WOULD BE THE MANUAL WAY TO USE VIEWSETS
#
# profile_list = views.ProfileViewSet.as_view({"get": "list"})
# profile_detail = views.ProfileViewSet.as_view({"get": "retrieve"})
#
# urlpatterns = [
#     path('profiles/', profile_list, name="profile-list"),
#     path('profiles/<int:pk>/', profile_detail, name="profile-detail"),
# ]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'status', views.ProfileStatusViewSet, basename='status')

urlpatterns = [
    path('', include(router.urls)),
    path('avatar/', views.AvatarUpdateView.as_view(), name="avatar-update")
]