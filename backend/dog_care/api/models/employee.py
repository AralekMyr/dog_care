from django.db import models

from api.models.care import Care
from api.models.center import Center
from api.models.person import Person


class Employee(Person):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    cares = models.ManyToManyField(Care)

    def __str__(self):
        return f"({self.id}) {self.center}"
