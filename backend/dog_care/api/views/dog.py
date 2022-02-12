from datetime import datetime

from django.db import transaction
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from api.models.dog import Dog
from api.serializers.dog import DogSerializer
from api.services import dog as dog_service
from api.views.permissions import IsPerson, IsDogOwner


class DogView(ListCreateAPIView):
    permission_classes = [IsPerson]
    serializer_class = DogSerializer

    def get_queryset(self):
        person = self.request.user.person
        return person.dogs.all().select_related("breed")

    def create(self, request, *args, **kwargs):
        person = request.user.person
        name = dog_service.get_name(request)
        birth_date = dog_service.get_birth_date(request)
        breed = dog_service.get_breed(request)

        with transaction.atomic():
            dog = Dog.objects.create(name=name, birth_date=birth_date, breed=breed, owner=person)
            data = self.get_serializer(dog).data

        return Response(data, status=status.HTTP_201_CREATED)


class DogDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsDogOwner]
    lookup_url_kwarg = 'id'
    serializer_class = DogSerializer

    def get_queryset(self):
        person = self.request.user.person
        return person.dogs.all()

    def patch(self, request, *args, **kwargs):
        dog = self.get_object()
        name = dog_service.get_name(request, dog)
        breed = dog_service.get_breed(request, dog)
        birth_date = dog_service.get_birth_date(request, dog)
        with transaction.atomic():
            if name:
                dog.name = name
            if breed:
                dog.breed = breed
            if birth_date:
                dog.birth_date = birth_date

            dog.save()
            dog.refresh_from_db()
            data = self.get_serializer(dog).data

        return Response(data, status=status.HTTP_200_OK)