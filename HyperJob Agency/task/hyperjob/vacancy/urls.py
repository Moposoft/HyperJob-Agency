from django.urls import path
from .views import VacanciesView, CreateVacancy

urlpatterns = [
    path('', VacanciesView.as_view()),
    path('new/', CreateVacancy.as_view()),
]