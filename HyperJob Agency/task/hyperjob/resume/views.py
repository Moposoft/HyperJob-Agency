from django.views import View
from django.shortcuts import render
from .models import Resume


class ResumesView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resume/index.html', {'resumes': resumes})
