from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Resume


class ResumesView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resume/index.html', {'resumes': resumes})


class CreateResume(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'resume/create.html')
        else:
            return HttpResponseForbidden()
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            resume = Resume.objects.create(
                author=request.user, description=request.POST.get('description'))
            return redirect('../../home')
        else:
            return HttpResponseForbidden()
