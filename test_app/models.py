from django.contrib.auth.models import User
from django.db import models
from simple_history import register
from simple_history.models import HistoricalRecords

from test_app_abstract.models import AbstractModel


class City(models.Model):
    name = models.CharField(max_length=50)
    history = HistoricalRecords()


class ConcreteModel(AbstractModel):
    concrete_field = models.CharField(max_length=50)


register(User)
