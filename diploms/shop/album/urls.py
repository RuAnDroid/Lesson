from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.projects, name="projects"),
    path('single-card/<str:pk>', views.single_card, name="single-card"),
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name="contact"),
    path('developers/', views.developers, name="developers"),


]
