from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.models.person import Person
from api.serializers.person import PersonSerializer


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
