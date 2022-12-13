from django.db import models

class Incident(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    datetime = models.DateTimeField()
    caseNumber = models.CharField(max_length = 15, blank=False, default='')
    description = models.TextField()
    location = models.TextField()

    def __unicode__(self):
        return self.caseNumber

    class Meta:
        ordering = ['created']
        