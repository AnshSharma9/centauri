from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),   # Add trailing slashes
    path('gallery/', views.gallery, name='gallery'),  # Add trailing slashes
    path('contact/', views.contact, name='contact'),  # Add trailing slashes
    path('login/', views.login, name='login'),
]
