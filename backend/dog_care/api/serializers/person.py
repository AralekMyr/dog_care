from rest_framework import serializers

from api.models.person import Person


class PersonSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Person
        fields = ["id", "first_name", "last_name", "username", "avatar"]
