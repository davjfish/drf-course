from rest_framework.serializers import ModelSerializer
from .. import models


class JobOfferSerializer(ModelSerializer):
    class Meta:
        model = models.JobOffer
        fields = "__all__"
