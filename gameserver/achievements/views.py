from django.shortcuts import render
from database.models import Achievement, PlayerAchievement, Player
from django.contrib.auth.decorators import login_required


@login_required
def all_achievements(request):
    current_user = request.user.id
    player_achievemets = PlayerAchievement.objects.filter(player_id=current_user)
    achieved_achievement_ids = [pa.achievement_id.id for pa in player_achievemets]

    achieved_achievements = Achievement.objects.filter(id__in=achieved_achievement_ids)
    unachieved_achievements = Achievement.objects.exclude(id__in=achieved_achievement_ids)

    return render(request, "achievements/achievements.html", {"achieved": achieved_achievements, "unachieved": unachieved_achievements, "app_name": "achievements"})
