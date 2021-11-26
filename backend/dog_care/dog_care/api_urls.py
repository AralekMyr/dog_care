from django.urls import path

from api.views.center.center import CenterView
from api.views.center.center_cares import CenterCaresView
from api.views.center.center_employees import CenterEmployeesView

urlpatterns = [
    path('centers/', CenterView.as_view(), name="list_centers"),
    path('centers/<int:id>/cares', CenterCaresView.as_view(), name="list_centers_cares"),
    path('centers/<int:id>/employees', CenterEmployeesView.as_view(), name="list_centers_employees"),
]
