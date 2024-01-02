from django.urls import path
from api import views
 
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('post/', views.add_task, name='add-task'),
    path('get/', views.view_task, name='view_task'),
    path('put/<int:pk>/', views.update_task, name='update-task'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
]