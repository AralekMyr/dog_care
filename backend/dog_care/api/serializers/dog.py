from rest_framework import serializers

from api.models.dog import Dog
from api.serializers.breed import BreedSerializer
from api.serializers.person import PersonSerializer


class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    owner = PersonSerializer()

    class Meta:
        model = Dog
        fields = ["id", "name", "birth_date", "breed", "owner"]
