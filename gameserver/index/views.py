from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {"app_name": "index"}
    return render(request, "index/index.html", data)
