from django.db import models

class UploadTxt(models.Model):
    text = models.FileField(upload_to='txt')
