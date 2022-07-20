"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('propietario/<int:id>', views.obtener_propietario,
            name='obtener_propietario'),
        path('crear/propietario', views.crear_propietario,
            name='crear_propietario'),
        path('editar_propietario/<int:id>', views.editar_propietario,
            name='editar_propietario'),
        path('eliminar/propietario/<int:id>', views.eliminar_propietario,
            name='eliminar_propietario'),
        # numeros telefonicos
        path('crear/departamento', views.crear_departamento,
            name='crear_departamento'),
        path('editar/departamento/<int:id>', views.editar_departamento,
            name='editar_departamento'),
        path('crear/departamento/propietario/<int:id>',
            views.crear_departamento_propietario,
            name='crear_numero_telefonico_estudiante'),
        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
 ]
