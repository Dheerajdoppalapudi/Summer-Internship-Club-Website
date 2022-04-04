from django.contrib import admin
from .models import Profile, Event
from import_export.admin import ImportExportModelAdmin

admin.site.register(Profile)
# admin.site.register(Event)

@admin.register(Event)
class ViewAdmin(ImportExportModelAdmin):
    pass