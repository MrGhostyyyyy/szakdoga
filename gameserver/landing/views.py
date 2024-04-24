from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def landing(request):
    data = {"app_name": "landing", "user": request.user.name}
    return render(request, "landing/landing.html", data)