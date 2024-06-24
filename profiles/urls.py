from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('exam', views.exam , name='exam'),
    path('ave', views.rex ,name='ave'),
    path('save', views.programming ,name='save'),
    path('Exams', views.Exam_setter ,name='Exams'),
]
