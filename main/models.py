from django.db import models

# Create your models here.

class FileUpload(models.Model):
    file_description    = models.CharField(max_length = 250)
    file_upload         = models.FileField(upload_to='files/')

    class Meta:
        db_table = 'file_upload'