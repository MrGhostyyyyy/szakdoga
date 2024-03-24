from django.contrib import admin
from database.models import Card, Character, Achievement, PlayerAchievement, Player


# Register your models here.
admin.site.register(Card)
admin.site.register(Character)
admin.site.register(Achievement)
admin.site.register(PlayerAchievement)
admin.site.register(Player)
