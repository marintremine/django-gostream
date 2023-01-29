from django.db import models


class Programme(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    pp = models.ImageField(upload_to='programmes', blank = True, null= True)

    def __str__(self) -> str:
        return self.name