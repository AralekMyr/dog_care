from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.models.center import Center
from api.serializers.employee import EmployeeSerializer


class CenterEmployeesView(ListAPIView):
    queryset = Center.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        center = self.get_object()
        employees = center.employees.all().prefetch_related("cares").select_related("user", "center")  # optimize sql requests
        data = self.get_serializer(employees, many=True).data
        return Response(data, status=status.HTTP_200_OK)
