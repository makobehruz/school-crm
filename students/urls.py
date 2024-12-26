from django.urls import path
from . import views


app_name = 'students'


urlpatterns = [
    path('list/', views.student_list, name='list'),
    path('form/', views.student_form, name='form'),
    path('detail/<int:pk>/', views.student_detail, name='detail'),
    path('update/<int:pk>/', views.student_update, name='update'),
    path('delete/<int:pk>/', views.student_delete, name='delete'),

]