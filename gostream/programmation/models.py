from django.db import models


class Programme(models.Model):
    image = models.ImageField(upload_to='programme', blank=True)