from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobOfferListCreateAPIView.as_view(), name="job-list"),
    path('jobs/<int:pk>/', views.JobOfferDetailAPIView.as_view(), name="job-detail"),
]