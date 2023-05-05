from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.projects, name="projects"),
    path('single-card/<str:pk>', views.single_card, name="single-card"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.register_user, name='register'),
    path('contact/', views.contact, name="contact"),
    path('developers/', views.developers, name="developers"),


]
