
from django.contrib import admin
from django.urls import path
from realestateapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('agent-single/', views.agents, name='agents'),
    path('agents-grid/', views.grid, name='grid'),
    path('blog-grid/', views.blog, name='blog'),
    path('blog-single/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
    path('property-grid/', views.property, name='property'),
    path('proprties/', views.properties, name='properties'),
]
