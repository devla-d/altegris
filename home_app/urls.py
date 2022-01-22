
from django.urls import path



from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.about, name="about"),
    path('pricing/', views.pricing, name="pricing"),
    path('services/', views.services, name="services"),
    path('support/', views.support, name="support"),
]
