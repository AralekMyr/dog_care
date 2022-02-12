from rest_framework import serializers

from api.models.appointment import Appointment, AppointmentCare
from api.serializers.care import CareSerializer
from api.serializers.dog import DogSerializer


class AppointmentCareSerializer(serializers.ModelSerializer):
    care = CareSerializer()

    class Meta:
        model = AppointmentCare
        fields = ['care', 'performer', 'time', 'state']


class AppointmentSerializer(serializers.ModelSerializer):
    dog = DogSerializer()
    cares = AppointmentCareSerializer(source="appointment_cares", many=True)

    class Meta:
        model = Appointment
        fields = ['id', 'date', 'cares', 'dog']
