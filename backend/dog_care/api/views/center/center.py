from rest_framework.generics import ListAPIView

from api.models.center import Center
from api.serializers.center import CenterSerializer


class CenterView(ListAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer
