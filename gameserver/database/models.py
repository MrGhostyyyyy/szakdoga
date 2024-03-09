from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from enum import Enum

class Players(AbstractBaseUser):
    pass

class Achievements(models.Model):
    # AutoField will be generated automatically 
    # but this is more in line with specification
    id = models.AutoField(primary_key=True)
    # name wont be long for achievements 20 enough
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=255)
    image = models.TextField(max_length=100)

class PlayerAchievements(models.Model):
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    achievement_id = models.ForeignKey(Achievements, on_delete=models.CASCADE)

class Card(models.Model):
    # AutoField will be generated automatically 
    # but this is more in line with specification
    id = models.AutoField(primary_key=True)
    # name wont be long for cards 20 enough
    name = models.TextField(max_length=20)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField(max_length=255)
    # ../../pics/x.png
    image = models.TextField(max_length=100)
    # action, equipment, bang
    type = models.TextField(max_length=10)
    # bandit or sherrif
    is_bandit = models.BooleanField()
    # BARREL, SNAKE, DYNAMITE, HORSESHOE
    symbol = models.TextField(max_length=10)    
    effect = models.TextField(max_length=100)
    # how many times it occured
    occurence = models.IntegerField(default=1)

class Character(Card):
    hit_points = models.IntegerField

class Symbols(Enum):
    BARREL = 1,
    SNAKE = 2,
    DYNAMITE = 3,
    HORSESHOE = 4,

class Effect(Enum):
    PULL = 1,
    BANG = 2,
    DODGE = 3,
    RELOAD = 4,
    ALWAYS = 5,
