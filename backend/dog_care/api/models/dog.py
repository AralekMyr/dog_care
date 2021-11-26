from django.db import models

from api.models.breed import Breed
from api.models.person import Person


class Dog(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    birth_date = models.DateField(null=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.id}) {self.name}, {self.owner.user.last_name}'s dog"
