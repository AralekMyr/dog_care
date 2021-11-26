from rest_framework import serializers

from api.models.employee import Employee
from api.serializers.care import CareSerializer
from api.serializers.center import CenterSerializer
from api.serializers.person import PersonSerializer


class EmployeeSerializer(PersonSerializer):
    cares = CareSerializer(many=True)
    center = CenterSerializer()

    class Meta:
        model = Employee
        fields = PersonSerializer.Meta.fields + ["center", "cares"]
