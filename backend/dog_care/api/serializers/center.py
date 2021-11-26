from rest_framework import serializers

from api.models.center import Center


class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = "__all__"
