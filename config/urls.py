"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicio
    path('',views.home, 
        name='home'),

    # Página de registro
    path('signup/',views.signup,
        name='signup'),

    # Página de tareas
    path('tasks/',views.tasks,
        name='tasks'),

    # Página de creación de tareas
    path('tasks/create/',views.create_task,
        name='create_task'),

    # Página de tareas completadas
    path('tasks_completed/',views.tasks_completed,
        name='tasks_completed'),

    # Página de detalle de tareas
    path('tasks/<int:task_id>/',views.task_detail,
        name='task_detail'),

    # Página de completar tareas
    path('tasks/<int:task_id>/complete',views.complete_task,
        name='complete_task'),

    # Página de eliminar tareas
    path('tasks/<int:task_id>/delete',views.delete_task,
        name='delete_task'),
    
    # Página de cerrar sesión
    path('logout/',views.signout,
        name='logout'),

    # Página de iniciar sesión
    path('signin/',views.signin,
        name='signin'),
]



