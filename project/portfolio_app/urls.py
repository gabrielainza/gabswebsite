from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iris/', views.iris, name='iris'),
    path('casa/', views.casa, name='casa'),
    path('descargar_cv/', views.descargar_cv, name='descargar_cv'),
]