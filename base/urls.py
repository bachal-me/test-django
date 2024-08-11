from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='portfolio'),
    path('projects/<slug:title>', views.caseStudy, name='case-study'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('services/<str:service>/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
