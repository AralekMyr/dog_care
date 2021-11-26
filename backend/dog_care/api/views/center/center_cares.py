from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.models.care import Care
from api.models.center import Center
from api.serializers.care import CareSerializer


class CenterCaresView(ListAPIView):
    queryset = Center.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = CareSerializer

    def get(self, request, *args, **kwargs):
        center = self.get_object()
        cares = Care.objects.filter(employee__center=center).distinct()
        data = self.get_serializer(cares, many=True).data
        return Response(data, status=status.HTTP_200_OK)
