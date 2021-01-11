from django.views import View
from .models import Vacancy
from django.shortcuts import render


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy/index.html', {'vacancies': vacancies})


