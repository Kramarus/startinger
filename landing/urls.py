from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_home, name="home"),
    path('services', views.render_services, name="services"),
    path('about', views.render_about, name="about"),
    path('contact', views.render_contact, name="contact"),
    path('quote', views.render_quote, name="quote")
]