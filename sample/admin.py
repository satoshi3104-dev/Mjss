from django.contrib import admin
from .models import house
from .models import station1
from .models import regionInfo1

# Register your models here.

admin.site.register(house)
admin.site.register(station1)
admin.site.register(regionInfo1)