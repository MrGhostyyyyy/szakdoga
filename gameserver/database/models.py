from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Players(AbstractBaseUser):
    pass

class Achievements(models.Model):
    # AutoField will be generated automatically 
    # but this is more in line with specification
    id = models.AutoField(primary_key=True)
    # name wont be long for achievements 20 enough
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=255)

class PlayerAchievements(models.Model):
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    achievement_id = models.ForeignKey(Achievements, on_delete=models.CASCADE)

class Card(models.Model):
    # AutoField will be generated automatically 
    # but this is more in line with specification
    id = models.AutoField(primary_key=True)
    # name wont be long for cards 20 enough
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=255)
