from django.contrib import admin
from django.urls import path, include 
from django.views.generic import RedirectView
from landing.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/index')),
    path('index/', include("index.urls")),
    path('achievements/', include("achievements.urls")),
    path('', include('django.contrib.auth.urls')),
    path('signup/', include("signup.urls")),
    path('game/', include("game.urls")),
    path('landing/', landing, name="landing")
]
