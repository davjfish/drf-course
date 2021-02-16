from rest_framework import serializers
from .. import models


class ProfileStatusSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.ProfileStatus
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)
    statuses = ProfileStatusSerializer(many=True, read_only=True)

    class Meta:
        model = models.Profile
        fields = "__all__"


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ["avatar"]
