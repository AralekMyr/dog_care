from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True)

    def __str__(self):
        return f"({self.id}) {self.user.first_name} {self.user.last_name} aka {self.user.username}"
