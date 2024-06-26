from django.urls import reverse_lazy
from django.views import generic

from database.forms import PlayerCreationForm

class SignUpView(generic.CreateView):
    form_class = PlayerCreationForm
    success_url = reverse_lazy("landing")
    template_name = "registration/signup.html"
