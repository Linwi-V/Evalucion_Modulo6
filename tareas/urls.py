from django.urls import path
from . import views

app_name = 'tareas'

urlpatterns = [
   path('', views.lista_tareas, name='lista'),
   path('crear/', views.crear_tarea, name='crear'),
   path('<int:tarea_id>/', views.detalle_tarea, name='detalle'),
   path('<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar'),

   # Autenticación
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]