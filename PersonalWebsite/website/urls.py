from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('cover/', views.cover, name="cover"),
    path('about/', views.about, name="about"),
    path('projects/', views.project_index, name="project_index"),
    path('work/', views.work, name="work"),
    path('resume/', views.resume, name="resume")
]