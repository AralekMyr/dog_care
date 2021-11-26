from rest_framework import serializers

from api.models.employee import Employee
from api.serializers.care import CareSerializer
from api.serializers.center import CenterSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    cares = CareSerializer(many=True)
    center = CenterSerializer()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "username", "avatar", "center", "cares"]
