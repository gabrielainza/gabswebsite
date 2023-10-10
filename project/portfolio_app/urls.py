from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('iris/', views.iris, name='iris'),
    path('casa/', views.casa, name='casa'),
    path('descargar_cv/', views.descargar_cv, name='descargar_cv'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
