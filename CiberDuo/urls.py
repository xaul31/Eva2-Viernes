"""
URL configuration for CiberDuo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contenido import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('preguntas/', views.PreguntaListView.as_view(), name='lista_preguntas'),
    path('preguntas/crear/', views.PreguntaCreateView.as_view(), name='crear_pregunta'),
    path('preguntas/<int:pk>/editar/', views.PreguntaUpdateView.as_view(), name='editar_pregunta'),
    path('preguntas/<int:pk>/eliminar/', views.PreguntaDeleteView.as_view(), name='eliminar_pregunta'),
    path('panel/', views.PanelAdminView.as_view(), name='panel_admin'),
    path('perfiles/', views.PerfilListView.as_view(), name='lista_perfiles'),
    path('perfiles/crear/', views.PerfilCreateView.as_view(), name='crear_perfil'),
    path('perfiles/<int:pk>/editar/', views.PerfilUpdateView.as_view(), name='editar_perfil'),
    path('perfiles/<int:pk>/eliminar/', views.PerfilDeleteView.as_view(), name='eliminar_perfil'),
    path('amenaza/', views.TipoAmenazaListView.as_view(), name='lista_amenazas'),
    path('amenaza/crear/', views.TipoAmenazaCreateView.as_view(), name='crear_amenaza'),
    path('amenaza/<int:pk>/editar/', views.TipoAmenazaUpdateView.as_view(), name='editar_amenaza'),
    path('amenaza/<int:pk>/eliminar/', views.TipoAmenazaDeleteView.as_view(), name='eliminar_amenaza'),
    path('medios/', views.MedioListView.as_view(), name='lista_medios'),
    path('medios/crear/', views.MedioCreateView.as_view(), name='crear_medio'),
    path('medios/<int:pk>/editar/', views.MedioUpdateView.as_view(), name='editar_medio'),
    path('medios/<int:pk>/eliminar/', views.MedioDeleteView.as_view(), name='eliminar_medio'),
]
