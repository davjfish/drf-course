from rest_framework import generics
from ..models import Quote
from .serializers import QuoteSerializer
from .permissions import IsAdminUserOrReadOnly

class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    permission_classes = [IsAdminUserOrReadOnly]

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]

#
# class ReviewCreateAPIView(generics.CreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [IsCorrectUserOrReadOnly]
#
#     def perform_create(self, serializer):
#         ebook_pk = self.kwargs.get("ebook_pk")
#         ebook = get_object_or_404(Ebook, pk=ebook_pk)
#         review_author = self.request.user
#         review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)
#         if review_queryset.exists():
#             raise ValidationError("You have already reviewed this book")
#
#         serializer.save(ebook=ebook, review_author=review_author)
#
#
# class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [IsCorrectUserOrReadOnly]
#
#
# # this is the breakdown of the concrete view class used above
# # class EbookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
# #     queryset = Ebook.objects.all()
# #     serializer_class = EbookSerializer
# #
# #     def get(self, request, *args, **kwargs):
# #         return self.list(request, *args, **kwargs)
# #
# #     def post(self, request, *args, **kwargs):
# #         return self.create(request, *args, **kwargs)