from django.urls import path
from . import views
urlpatterns=[
    path('',views.mainpage,name='main'),
    path('index',views.index,name='index'),
    path('add',views.addpage,name='addarticle'),
    path('edit/<int:uid>',views.editpage,name='edit'),
    path('del/<int:uid>',views.delete,name='del'),
    path('update',views.update,name='update')
]