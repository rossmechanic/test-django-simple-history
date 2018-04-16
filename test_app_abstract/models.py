from django.db import models

from simple_history.models import HistoricalRecords


class AbstractModel(models.Model):
    name_field = models.CharField(max_length=50)
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
