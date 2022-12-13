from rest_framework import serializers
from apis.models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = [
            'id',
            'created',
            'datetime',
            'caseNumber',
            'description',
            'location'
        ]
