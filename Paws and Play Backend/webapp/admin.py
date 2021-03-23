from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(adoption_request)

@admin.register(adoption)
class adoptionAdmin(ImportExportModelAdmin):
    pass

