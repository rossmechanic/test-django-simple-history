from django.contrib.admin import register
from simple_history.admin import SimpleHistoryAdmin

from test_app.models import City


@register(City)
class CityAdmin(SimpleHistoryAdmin):
    pass
