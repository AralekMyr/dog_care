from django.db import transaction
from django.db.models import Prefetch
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView

from api.models.appointment import Appointment, AppointmentCare
from api.serializers.appointment import AppointmentSerializer
from api.services import appointment as appointment_service
from api.views.permissions import IsPerson


class AppointmentView(ListCreateAPIView):
    permission_classes = [IsPerson]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        person = self.request.user.person
        if person.is_employee():
            employee = person.as_employee()
            queryset = Appointment.objects.filter(cares__appointment_cares__performer=employee)
        else:
            queryset = Appointment.objects.filter(dog__owner=person)

        return queryset.select_related(
            "dog", "dog__owner__user", "dog__breed"
        ).prefetch_related(
            Prefetch("appointment_cares", queryset=AppointmentCare.objects.select_related("care"))
        )

    def create(self, request, *args, **kwargs):
        date = appointment_service.get_appointment_date(request)
        dog = appointment_service.get_dog(request)
        with transaction.atomic():
            appointment = Appointment.objects.create(date=date, dog=dog)
            cares = request.data.get("cares")
            if not len(cares):
                raise ValidationError("You must have at least one care")
            for care in cares:
                appointment_service.add_care(care, appointment)
                print(care)
            raise