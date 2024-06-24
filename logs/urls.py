from django.urls import path, include
from . import views

urlpatterns = [
    path('signin', views.Login , name='signin'),
    path('signup', views.signup , name='signup'),
    path('setup', views.setup , name='setup'),
]
