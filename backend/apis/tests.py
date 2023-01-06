from django.test import TestCase
from django.urls import reverse
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model

from .models import Incident
from .admin import IncidentAdmin

from rest_framework.test import APIClient

from datetime import datetime

class IncidentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        User = get_user_model()
        self.user = User.objects.create_superuser(
            username='mpruss',
            email='mpruss@dzr.de',
            password='hunter2')
        self.client.force_login(user=self.user)

    def create_incident(
        self,
        created = datetime.now(),
        datetime = datetime(1937, 5, 6, 19, 25),
        caseNumber = 'ABC123',
        description = 'Gross Negligance and Hubris',
        location = 'NAS Lakehurst, Manchester Township, New Jersey, U.S.',
        latitude = 39.977818000,
        longitude = -74.331928700
    ):
        return Incident.objects.create(
            created = created,
            datetime = datetime,
            caseNumber = caseNumber,
            description = description,
            location = location,
            latitude = latitude,
            longitude = longitude
        )

    # Models
    def test_incident_creation(self):
        i = self.create_incident()
        self.assertTrue(isinstance(i, Incident))
        self.assertEqual(i.__unicode__(), i.caseNumber)

    def test_return_caseNumber(self):
        i = self.create_incident()
        caseNumber = i.__unicode__()
        self.assertEqual(caseNumber, i.caseNumber)

    # Views
    def test_incident_list_view(self):
        i = self.create_incident()
        url = reverse('incident_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(i.caseNumber, response.content.decode("utf-8"))

    def test_create_read_incident_view(self):
        i = self.create_incident()
        url = reverse('incident', args=[i.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(i.caseNumber, response.content.decode("utf-8"))

    def test_create_update_incident_view(self):
        i = self.create_incident()
        url = reverse('incident', args=[i.id])
        response = self.client.get(url)

        updated_incident = {
            'datetime': i.datetime,
            'caseNumber': i.caseNumber,
            'description': "An updated description",
            'location': i.location,
            'latitude': i.latitude,
            'longitude': i.longitude
        }

        response = self.client.put(url, data=updated_incident)

        self.assertEqual(response.status_code, 200)
        self.assertIn(i.caseNumber, response.content.decode("utf-8"))
        self.assertIn(updated_incident['description'], response.content.decode("utf-8"))

    def test_delete_incident_view(self):
        i = self.create_incident()
        url = reverse('incident', args=[i.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

class CustomIncidentAdmin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.incident = Incident.objects.create(
            created = datetime.now(),
            datetime = datetime(1937, 5, 6, 19, 25),
            caseNumber = 'ABC123',
            description = 'Gross Negligance and Hubris',
            location = 'NAS Lakehurst, Manchester Township, New Jersey, U.S.',
            latitude = 39.977818000,
            longitude = -74.331928700
        )

    def setUp(self):
        self.site = AdminSite()

    def test_IncidentAdmin_str(self):
        incident_admin = IncidentAdmin(Incident, self.site)
        self.assertEqual(str(incident_admin), 'apis.IncidentAdmin')

class IncidentPermissions(TestCase):
    def setUp(self):
        self.client = APIClient()

        User = get_user_model()
        self.user = User.objects.create_user(
            username='mpruss',
            email='mpruss@dzr.de',
            password='hunter2')
        self.client.force_login(user=self.user)

    def create_incident(
        self,
        created = datetime.now(),
        datetime = datetime(1937, 5, 6, 19, 25),
        caseNumber = 'ABC123',
        description = 'Gross Negligance and Hubris',
        location = 'NAS Lakehurst, Manchester Township, New Jersey, U.S.',
        latitude = 39.977818000,
        longitude = -74.331928700
    ):
        return Incident.objects.create(
            created = created,
            datetime = datetime,
            caseNumber = caseNumber,
            description = description,
            location = location,
            latitude = latitude,
            longitude = longitude
        )

    def test_incident_creation_user_403(self):
        incident = {
            'datetime': datetime.now(),
            'caseNumber': datetime(1937, 5, 6, 19, 25),
            'description': 'ABC123',
            'location': 'NAS Lakehurst, Manchester Township, New Jersey, U.S.',
            'latitude': 39.977818000,
            'longitude': -74.331928700
        }

        url = reverse('incident_list')
        response = self.client.put(url, data=incident)

        self.assertEqual(response.status_code, 403)

    # Views
    def test_incident_list_view_user_200(self):
        i = self.create_incident()
        url = reverse('incident_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(i.caseNumber, response.content.decode("utf-8"))

    def test_create_read_incident_view_user_200(self):
        i = self.create_incident()
        url = reverse('incident', args=[i.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(i.caseNumber, response.content.decode("utf-8"))

    def test_create_update_incident_view_user_403(self):
        i = self.create_incident()
        url = reverse('incident', args=[i.id])
        response = self.client.get(url)

        updated_incident = {
            'datetime': i.datetime,
            'caseNumber': i.caseNumber,
            'description': "An updated description",
            'location': i.location,
            'latitude': i.latitude,
            'longitude': i.longitude
        }

        response = self.client.put(url, data=updated_incident)

        self.assertEqual(response.status_code, 403)

    def test_delete_incident_view_user_403(self):
        i = self.create_incident()
        url = reverse('incident', args=[i.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)