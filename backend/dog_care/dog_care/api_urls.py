from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from api.views.appointment import AppointmentView
from api.views.center.center import CenterView
from api.views.center.center_cares import CenterCaresView
from api.views.center.center_employees import CenterEmployeesView
from api.views.dog import DogView, DogDetailView
from api.views.user import UserView, UserDetailView

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', UserView.as_view(), name="create_user"),
    path('users/<int:id>', UserDetailView.as_view(), name="user_detail"),

    path('centers/', CenterView.as_view(), name="list_centers"),
    path('centers/<int:id>/cares', CenterCaresView.as_view(), name="list_centers_cares"),
    path('centers/<int:id>/employees', CenterEmployeesView.as_view(), name="list_centers_employees"),

    path('user/dogs', DogView.as_view(), name="user_dogs"),
    path('user/dogs/<int:id>', DogDetailView.as_view(), name="user_dog_detail"),

    path('appointments', AppointmentView.as_view(), name="appointments"),
]
