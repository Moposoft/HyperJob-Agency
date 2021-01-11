from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/index.html')


class UserCreationView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'hyperjob/signup.html'


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'