from django.forms import ModelForm
from .models import Player, Achievement, Card, Character, PlayerAchievement


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = "__all__"


class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        fields = "__all__"


class PlayerAchievementForm(ModelForm):
    class Meta:
        model = PlayerAchievement
        fields = "__all__"


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = "__all__"


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = "__all__"
