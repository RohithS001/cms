from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


@admin.register(Event)
class EventsAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fields = [
                ('name', 'slug'),
                ('date', 'creator', 'album'),
                'content'
             ]

    list_display = ('name', 'slug', 'date', 'creator')
