from django.urls import path

from . import views

urlpatterns = [
    path("quotes/", views.QuoteListCreateAPIView.as_view(), name="quote-list"),
    path("quotes/<int:pk>/", views.QuoteDetailAPIView.as_view(), name="quote-detail"),
    # path("ebooks/<int:ebook_pk>/review/", ReviewCreateAPIView.as_view(), name="ebook-review"),
    # path("review/<int:pk>/", ReviewDetailAPIView.as_view(), name="review-detail"),
]
