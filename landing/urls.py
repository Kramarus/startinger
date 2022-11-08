from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_home, name="home"),
    path('services', views.render_services, name="services"),
    path('about', views.render_about, name="about"),
    path('contact', views.CreateContact.as_view(), name="contact"),
    path('quote', views.CreateApplicant.as_view(), name="quote"),
    path('thankyou', views.render_thankyou, name="thankyou"),
]