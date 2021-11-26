from django.contrib import admin

# Register your models here.
from api.models.appointment import Appointment, AppointmentCare
from api.models.breed import Breed
from api.models.care import Care
from api.models.center import Center
from api.models.dog import Dog
from api.models.employee import Employee
from api.models.person import Person

admin.site.register(Appointment)
admin.site.register(AppointmentCare)
admin.site.register(Breed)
admin.site.register(Care)
admin.site.register(Center)
admin.site.register(Dog)
admin.site.register(Employee)
admin.site.register(Person)
