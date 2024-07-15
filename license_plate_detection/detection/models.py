# detection/models.py

from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    plate_text = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.file.name
