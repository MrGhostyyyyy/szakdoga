from django.shortcuts import render


def index(request):
    data = {"app_name": "index"}
    return render(request, "index/index.html", data)
