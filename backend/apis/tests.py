import csv
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Incident
from .admin import IncidentAdmin, CsvImportForm

from rest_framework.test import APIClient

from datetime import datetime
import os

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
        location = 'NAS Lakehurst, Manchester Township, New Jersey, U.S.'
    ):
        return Incident.objects.create(
            created = created,
            datetime = datetime,
            caseNumber = caseNumber,
            description = description,
            location = location
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
            'location': i.location
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
            location = 'NAS Lakehurst, Manchester Township, New Jersey, U.S.'
        )

    def setUp(self):
        self.site = AdminSite()

    def test_IncidentAdmin_str(self):
        incident_admin = IncidentAdmin(Incident, self.site)
        self.assertEqual(str(incident_admin), 'apis.IncidentAdmin')

class IncidentPermissions(TestCase):
    pass