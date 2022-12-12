from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient

from .models import Incident
from datetime import datetime

class IncidentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()


    def create_incident(
        self,
        created = datetime.now(),
        datetime = datetime(1937, 5, 6, 19, 25),
        caseNumber = 'ABC123',
        description = 'Gross Negligance and Hubris',
        location = 'NAS Lakehurst, Manchester Township, New Jersey, U.S.'
    ):
        return Incident.objects.create(
            created = created,
            datetime = datetime,
            caseNumber = caseNumber,
            description = description,
            location = location
        )
    
    # Model
    def test_incident_creation(self):
        i = self.create_incident()
        self.assertTrue(isinstance(i, Incident))
        self.assertEqual(i.__unicode__(), i.caseNumber)

    # View
    def test_incident_list_view(self):
        i = self.create_incident()
        url = reverse('incident_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        import pdb; pdb.set_trace()
        self.assertIn(i.caseNumber, response.content.decode("utf-8"))