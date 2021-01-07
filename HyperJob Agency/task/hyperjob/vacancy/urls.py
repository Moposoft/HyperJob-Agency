from django.urls import path
from .views import VacanciesView

urlpatterns = [
    path('', VacanciesView.as_view()),
]