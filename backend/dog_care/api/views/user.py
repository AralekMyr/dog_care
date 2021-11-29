from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from api.models.person import Person
from api.serializers.person import PersonSerializer
from api.views.permissions import IsConnectedUser


class UserView(CreateAPIView):
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                        email=email, password=password)
        person = Person.objects.create(user=user)

        data = self.get_serializer(person).data
        return Response(data, status=status.HTTP_201_CREATED)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsConnectedUser]
    queryset = Person.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = PersonSerializer

    def patch(self, request, *args, **kwargs):
        person = self.get_object()
        user = person.user
        with transaction.atomic():
            if request.data.get("first_name"):
                user.first_name = request.data.get("first_name")
            if request.data.get("last_name"):
                user.last_name = request.data.get("last_name")
            if request.data.get("email"):
                user.email = request.data.get("email")
            if request.data.get("password"):
                user.set_password(request.data.get("password"))
            user.save()

        person.refresh_from_db()
        data = self.get_serializer(person).data
        return Response(data, status=status.HTTP_200_OK)
