from django.urls import path
from . import views


app_name = 'subjects'


urlpatterns = [
    path('list/', views.subject_list, name='list'),
    path('form/', views.subject_form, name='form'),
    path('detail/<int:pk>/', views.subject_detail, name='detail'),
    path('update/<int:pk>/', views.subject_update, name='update'),
    path('delete/<int:pk>/', views.subject_delete, name='delete'),
]