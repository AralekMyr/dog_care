from rest_framework import serializers

from api.models.care import Care


class CareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Care
        fields = "__all__"
