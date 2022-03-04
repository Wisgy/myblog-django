from django.urls import path
from django.contrib import admin
from . import views
urlpatterns=[
    path('',views.mainpage,name='main'),
    path('index',views.index,name='index'),
    path('addcomment/<int:uid>',views.addpage,name='addpage'),
    path('add',views.add,name='add'),
    # path('del/<int:uid>',views.delete,name='delete'),
    # path('update',views.update,name='update'),
    path('browse/<int:uid>',views.browse,name='browse'),
]