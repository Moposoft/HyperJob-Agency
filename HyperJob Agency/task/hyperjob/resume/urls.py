from django.urls import path
from .views import ResumesView, CreateResume

urlpatterns = [
    path('', ResumesView.as_view()),
    path('new/', CreateResume.as_view())
]