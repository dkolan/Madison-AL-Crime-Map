# Generated by Django 4.1.3 on 2022-12-22 18:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datetime', models.DateTimeField()),
                ('caseNumber', models.CharField(default='', max_length=15)),
                ('description', models.TextField()),
                ('location', models.TextField()),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
