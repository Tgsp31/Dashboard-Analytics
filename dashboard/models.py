from django.db import models

# Create your models here.


class DataPoint(models.Model):
    end_year = models.CharField(max_length=10, blank=True, null=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100, blank=True, null=True)
    topic = models.CharField(max_length=100)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=100, blank=True, null=True)
    start_year = models.CharField(max_length=10, blank=True, null=True)
    impact = models.CharField(max_length=100, blank=True, null=True)
    added = models.DateTimeField()
    published = models.DateTimeField()
    country = models.CharField(max_length=100, blank=True, null=True)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100)
    title = models.TextField()
    likelihood = models.IntegerField()

    def __str__(self):
        return self.title
