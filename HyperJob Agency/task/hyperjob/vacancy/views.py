from django.views import View
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Vacancy


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy/index.html', {'vacancies': vacancies})


class CreateVacancy(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            return render(request, 'vacancy/create.html')
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            resume = Vacancy.objects.create(
                author=request.user, description=request.POST.get('description'))
            return redirect('../../home')
        else:
            return HttpResponseForbidden()