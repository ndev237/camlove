from django.urls import path
from . import views

app_name = 'vitrine'

urlpatterns = [
    path('', views.about, name="about"),
    path('', views.contact, name="contact"),
]
