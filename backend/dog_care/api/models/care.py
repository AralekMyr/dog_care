from django.db import models


class Care(models.Model):
    name = models.CharField(max_length=200)
    duration = models.DurationField(null=False)
    price = models.FloatField(null=False)

    def __str__(self):
        return f"({self.id}) {self.name} - {self.price}€"
