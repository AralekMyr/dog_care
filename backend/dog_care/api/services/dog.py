from datetime import datetime

from rest_framework.exceptions import ValidationError

from api.models.breed import Breed


def get_birth_date(request, dog=None):
    birth_date = request.data.get("birth_date")
    if not birth_date and dog:
        return None
    try:
        birth_date = datetime.strptime(birth_date, '%d/%m/%Y').date()
        if birth_date >= datetime.now().date():
            raise ValueError
    except(ValueError, TypeError):
        raise ValidationError("Invalid birth_date")


def get_breed(request, dog=None):
    breed = request.data.get("breed")
    if not breed and dog:
        return None
    try:
        return Breed.objects.get(id=breed)
    except(ValueError, TypeError, Breed.DoesNotExist):
        raise ValidationError("Invalid breed id")


def get_name(request, dog=None):
    name = request.data.get("name")
    if not name and dog:
        return None
    if not name:
        raise ValidationError("name cannot be empty")
    return name
