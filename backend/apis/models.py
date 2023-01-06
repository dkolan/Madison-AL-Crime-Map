from django.db import models

class Incident(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    datetime = models.DateTimeField()
    caseNumber = models.CharField(max_length = 15, blank=False, default='')
    description = models.TextField()
    location = models.TextField()
    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)

    def __unicode__(self):
        return self.caseNumber

    class Meta:
        ordering = ['created']
        unique_together = ['datetime', 'caseNumber', 'description', 'location', 'latitude', 'longitude']
        