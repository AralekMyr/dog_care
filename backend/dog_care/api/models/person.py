from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"({self.id}) {self.user.first_name} {self.user.last_name} aka {self.user.username}"

    def is_employee(self):
        return hasattr(self, 'employee')

    def as_employee(self):
        from api.models.employee import Employee
        try:
            return Employee.objects.get(person_ptr=self)
        except Employee.DoesNotExist:
            return None
