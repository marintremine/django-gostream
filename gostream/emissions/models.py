from django.db import models

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self) -> str:
        return self.name

class Emission(models.Model):
    name = models.CharField(max_length=64)
    schedule = models.CharField(max_length=64)
    hashtag = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    pp = models.ImageField(upload_to='emissions', blank = True, null= True)
    color = models.CharField(max_length=256,blank = True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name