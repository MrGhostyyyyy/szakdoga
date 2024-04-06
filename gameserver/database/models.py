"""
This file holds Django's necessary database related classes.
Django will use these models to interact with the database
it creates. Each class represents a Table in the database
and their variables represent a column. The data will be
stored in a ``db.sqlite3`` database file and it will be loaded
from ``.csv`` files using ``scripts/load_csv.py``.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import PlayerManager

class Player(AbstractBaseUser, PermissionsMixin):
    """
    ``Players Model`` class for Django's database.
    This stores the information of every user.
    """
    objects = PlayerManager()

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=20, unique=True)
    profile_pic = models.TextField(max_length=30)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'name'
    NAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return f"{self.id} {self.name} - {self.password} - {self.profile_pic}"


class Achievement(models.Model):
    """
    ``Achievements Model`` class for Django's database.
    This stores the achievements in the game.
    """

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=20, unique=True)
    description = models.TextField(max_length=255)
    image = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.name} - {self.description} - {self.image}"


class PlayerAchievement(models.Model):
    """
    ``PlayerAchievements Model`` class for Django's database.
    This is a linking table linking the player by their achieved achievements.
    """

    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    achievement_id = models.ForeignKey(Achievement, on_delete=models.CASCADE)

    def __str__(self):
        try:
            player = Player.objects.get(id=self.player_id)
            achievement = Achievement.objects.get(id=self.achievement_id)
            return f"{player.name} - {achievement.name}"
        except Player.DoesNotExist:
            return None
        except Achievement.DoesNotExist:
            return None


class Card(models.Model):
    r"""
    ``Card Model`` class for Django's database.
    This contains the data of every card.
    """

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=20, unique=True)
    description = models.TextField(max_length=280)
    image = models.TextField(max_length=100)
    type = models.TextField(max_length=10)
    symbol = models.TextField(max_length=10)
    bandit_occurence = models.IntegerField(default=0)
    cowboy_occurence = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} {self.name} - {self.description} - {self.image} - {self.type} - {self.symbol} - {self.bandit_occurence} - {self.cowboy_occurence}"


class Character(models.Model):
    """
    ``Character Model`` class for Django's database.
    Stores the data of every character card.
    """
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=20, unique=True)
    description = models.TextField(max_length=255)
    image = models.TextField(max_length=30)
    hit_points = models.IntegerField(default=3)
    is_bandit = models.BooleanField()

    def __str__(self):
        return f"{self.id} {self.name} - {self.description} - {self.image} - {self.is_bandit} - {self.hit_points}"
