from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user 
from todolist.views import logout_user 
from todolist.views import new_list,add 
from todolist.views import finish_task,delete_task,json


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('json/', json, name='json'),
    path('add/', add, name='add'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', new_list, name='new_list'),
    path('finish-task/<int:pk>/', finish_task, name='finish'),
    path('delete-task/<int:pk>/', delete_task, name='delete'),
]