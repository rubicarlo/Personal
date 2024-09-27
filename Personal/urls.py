import debug_toolbar
from django.contrib import admin
from django.urls import include, path
from BusquedaPersonal import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('personas/', views.personas_list, name='personas_list'),
    path('api/personas/filtrar/', views.personas_filtrar, name='personas_filtrar'),  # Nueva URL para el filtro
    path('picha/', views.personas_list, name='picha'),

    path('__debug__/', include(debug_toolbar.urls)),
]
