from rest_framework import serializers

from ..models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Quote
        fields = "__all__"
