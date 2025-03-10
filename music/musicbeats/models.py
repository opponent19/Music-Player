from django.db import models

# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    song = models.FileField(upload_to='images')
    
