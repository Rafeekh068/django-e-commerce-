from django.db import models

# theme model.

class SiteSettings(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()
    