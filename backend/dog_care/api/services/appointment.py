from datetime import datetime

from rest_framework.exceptions import ValidationError

from api.models.care import Care
from api.models.center import Center
from api.models.dog import Dog
from api.models.employee import Employee


def get_appointment_date(request):
    date = request.data.get("date")
    try:
        date = datetime.strptime(date, '%d/%m/%Y').date()
        if date < datetime.now().date():
            raise ValueError
        return date
    except(ValueError, TypeError):
        raise ValidationError("Invalid date")


def get_dog(request):
    person = request.user.person
    dog_id = request.data.get("dog")
    try:
        return person.dogs.get(id=dog_id)
    except(ValueError, TypeError, Dog.DoesNotExist):
        raise ValidationError("Invalid dog")


def get_center(request):
    center_id = request.data.get("center")
    try:
        return Center.objects.get(id=center_id)
    except(ValueError, TypeError, Center.DoesNotExist):
        raise ValidationError("Invalid center")


def get_performer(care_data, center):
    performer_id = care_data.get("performer")
    try:
        return Employee.objects.get(id=performer_id, center=center)
    except(ValueError, TypeError, Employee.DoesNotExist):
        raise ValidationError("Invalid performer")


def get_care(care_data, performer):
    care_id = care_data.get("care")
    try:
        care = Care.objects.get(id=care_id)
    except(ValueError, TypeError, Care.DoesNotExist):
        raise ValidationError("Invalid care")
    if care not in performer.cares.all():
        raise ValidationError("The performer cannot do this care")
    return care


def get_time(care_data, date):
    time_str = care_data.get("time")
    


def add_care(care_data, appointment):
    performer = get_performer(care_data, appointment.center)
    care = get_care(care_data, performer)
    time = get_time(care_data, appointment.date)