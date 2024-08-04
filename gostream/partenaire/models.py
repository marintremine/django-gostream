from django.db import models

# Create your models here.
class Partenaire(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    pp = models.ImageField(upload_to='partenaires', blank = True, null= True)
    
    twitch = models.CharField(max_length=256,blank = True)
    youtube = models.CharField(max_length=256,blank = True)
    twitter = models.CharField(max_length=256,blank = True)
    instagram = models.CharField(max_length=256,blank = True)
    tiktok = models.CharField(max_length=256,blank = True)
    discord = models.CharField(max_length=256,blank = True)
    facebook = models.CharField(max_length=256,blank = True)
    other = models.CharField(max_length=256,blank = True)

    def __str__(self) -> str:
        return self.name