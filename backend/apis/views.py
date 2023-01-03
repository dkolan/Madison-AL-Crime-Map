from apis.models import Incident
from apis.serializers import IncidentSerializer
from rest_framework.permissions import *
from rest_framework import permissions

from rest_framework import generics

class IncidentList(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [AllowAny()]
        return [permission() for permission in self.permission_classes]

class IncidentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [AllowAny()]
        return [permission() for permission in self.permission_classes]
