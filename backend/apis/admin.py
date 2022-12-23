from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms

from .models import Incident

class IncidentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'datetime',
        'caseNumber',
        'description',
        'location'
    )

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv)]
        print(f'urls = {urls}')
        print(f'new_urls = {new_urls}')
        print(f'new_urls + urls = {new_urls + urls}')
        return new_urls + urls

    def upload_csv(self, request):
        form = CsvImportForm()
        data = {'form': form}
        return render(request, 'admin/csv_upload.html', data)

admin.site.register(Incident, IncidentAdmin)

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()