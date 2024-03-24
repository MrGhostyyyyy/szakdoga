from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index(request):
    data = {"app_name": "login"}

    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = authenticate(request, name=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect("landing")
        else:
            data["error"] = "Hiba a bejelentkezésnél, próbáld újra!"
            return render(request, "login/login.html", data)
    else:
        return render(request, "login/login.html", data)
