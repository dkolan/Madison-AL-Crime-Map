from django import forms
from django.contrib import admin, messages
from django.urls import path, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import IntegrityError

from .models import Incident

from datetime import datetime

class IncidentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'datetime',
        'caseNumber',
        'description',
        'location',
        'latitude',
        'longitude'
    )

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv, name='upload_csv')]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_upload']

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'Invalid filetype. Please upload a CSV.')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode('utf-8')
            csv_data = file_data.split('\n')

            headers = csv_data[0]
            data = csv_data[1:]
            print(data[9].split(',')[2])
            for datum in data:
                vals = datum.split(',')
                try:
                    Incident.objects.create(
                        created = datetime.now(),
                        datetime =  datetime.strptime(vals[0], '%m/%d/%Y %I:%M:%S %p'),
                        caseNumber = vals[1],
                        description = vals[2],
                        location = vals[3],
                        latitude = vals[4],
                        longitude = vals[5]
                    )
                except IntegrityError:
                    print('Duplicate Value.')

            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {'form': form}
        return render(request, 'admin/csv_upload.html', data)

admin.site.register(Incident, IncidentAdmin)

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()