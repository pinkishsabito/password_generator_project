from django.urls import path

from generator import views


urlpatterns = [
    path('/', views.password, name='password'),
    path('/about', views.about, name='about'),
    path('/generate', views.generate, name='generate'),
]
