from django.db import models

# Create your models here.
class Partenaire(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    pp = models.ImageField(upload_to='partenaires', blank = True, null= True)

    def __str__(self) -> str:
        return self.name