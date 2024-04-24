from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include 
from django.views.generic import RedirectView
from landing.views import landing
from index.views import index

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', RedirectView.as_view(url='/index')),
    path('index/', index, name="index"),
    path('achievements/', include("achievements.urls"), name="achievements"),
    path('signup/', include("signup.urls"), name="signup"),
    path('game/', include("game.urls")),
    path('landing/', landing, name="landing"),
    path('', include('django.contrib.auth.urls'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('single/', include("single.urls"), name="single")
]
