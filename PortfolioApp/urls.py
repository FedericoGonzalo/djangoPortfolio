from django.contrib import admin
from django.urls import path
from PortfolioApp import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',views.home,name="Home"),
    path('experiencias',views.expe,name="Experiencias Laborales"),
    path('proyectos',views.proye,name="Proyectos"),
    path('contacto',views.contacto,name="Contacto"),
]
