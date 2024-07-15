from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at', 'plate_text')
