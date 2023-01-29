from django.db import models

# Create your models here.
class Streamer(models.Model):
    name = models.CharField(max_length=64)

    twitch = models.CharField(max_length=256,blank = True)
    youtube = models.CharField(max_length=256,blank = True)
    twitter = models.CharField(max_length=256,blank = True)
    instagram = models.CharField(max_length=256,blank = True)
    tiktok = models.CharField(max_length=256,blank = True)
    other = models.CharField(max_length=256,blank = True)

    pp = models.ImageField(upload_to='streamers', blank = True, null= True)

    def __str__(self) -> str:
        return self.name

class Equipe(models.Model):
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=128)
    twitch = models.CharField(max_length=256,blank = True)
    youtube = models.CharField(max_length=256,blank = True)
    twitter = models.CharField(max_length=256,blank = True)
    instagram = models.CharField(max_length=256,blank = True)
    tiktok = models.CharField(max_length=256,blank = True)
    other = models.CharField(max_length=256,blank = True)

    pp = models.ImageField(upload_to='equipes', blank = True, null= True)

    def __str__(self) -> str:
        return self.name