from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(user_login_details)

@admin.register(questionnaire)
class questionnaireAdmin(ImportExportModelAdmin):
    pass