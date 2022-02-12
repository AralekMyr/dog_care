from django.db import models

from api.models.care import Care
from api.models.center import Center
from api.models.dog import Dog
from api.models.employee import Employee


class Appointment(models.Model):
    ACTIVE = 1
    CANCELLED = 2
    DONE = 3

    TAB_STATES = {
        ACTIVE: "Active",
        CANCELLED: "Cancelled",
        DONE: "Done"
    }
    value = models.PositiveIntegerField(
        choices=TAB_STATES.items(), default=None, blank=True, null=True
    )

    date = models.DateField(null=False)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    cares = models.ManyToManyField(Care, through="AppointmentCare")
    state = models.PositiveIntegerField(choices=TAB_STATES.items(), default=ACTIVE)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name="appointments")

    def __str__(self):
        return f"Appointment for {self.dog.name}, the {self.date.strftime('%d/%m/%Y')}"


class AppointmentCare(models.Model):
    care = models.ForeignKey(Care, on_delete=models.CASCADE, related_name="appointment_cares")
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="appointment_cares")
    performer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="appointment_cares")
    time = models.TimeField(null=False)

    def __str__(self):
        return f"({self.id}) {self.care.name} at {self.time} for {self.appointment.dog.name}"
