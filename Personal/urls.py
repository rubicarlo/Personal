import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from BusquedaPersonal import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('personas/', views.PersonasListView.as_view(), name='personas_list'),
    path('api/personas/filtrar/', views.personas_filtrar, name='personas_filtrar'),
    path('picha/', views.personas_filtrar, name='picha'),
    path('personas/<str:dni>/', views.EditarPersonaView.as_view(), name='editar_persona'),
    path('vidalaboral/<str:dni>/', views.VidaLaboralView.as_view(), name='vidalaboral'),
    path('__debug__/', include(debug_toolbar.urls)),
]
