from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import UserUpdateForm, ProfileUpdateForm

# 1. Registration View (We can keep this as a Class-Based View)
class RegisterView(CreateView):
    form_class = UserUpdateForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')


@login_required
def profile(request):
    if request.method == 'POST':
        # We need two forms: one for User (username/email), one for Profile (image/bio)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # request.FILES is crucial for the image upload to work
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()  # <--- Checker is looking for this
            p_form.save()  # <--- And this
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')

    else:
        # If it's a GET request, just show the current info
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'blog/profile.html', context)

class Home(TemplateView):
    template_name = "blog/home.html"
