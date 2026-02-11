# blog/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileUpdateForm, RegisterForm


# 1. Registration View
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("home")


# 2. Profile Management View
class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = "blog/profile.html"
    success_url = reverse_lazy("profile") 

    # This method tells Django: "The object we are editing is the CURRENT user"
    def get_object(self):
        return self.request.user
    


class Home(TemplateView):
    template_name = "blog/home.html"

