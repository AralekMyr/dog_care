from django.db import models

from api.models.care import Care
from api.models.dog import Dog
from api.models.employee import Employee


class Appointment(models.Model):
    date = models.DateField(null=False)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    cares = models.ManyToManyField(Care, through="AppointmentCare")

    def __str__(self):
        return f"Appointment for {self.dog.name}, the {self.date.strftime('%d/%m/%Y')}"


class AppointmentCare(models.Model):
    care = models.ForeignKey(Care, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    performer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    time = models.TimeField(null=False)

    def __str__(self):
        return f"({self.id}) {self.care.name} at {self.time} for {self.appointment.dog.name}"
