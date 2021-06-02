from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/',views.index),
    path('HomePage/',views.HomePage),
    path('logOut/',views.loginOut),
    path('editor/',views.editor),
    path('detail/',views.detail),
    path('reEditor/',views.reEditor),
    path('test/',views.test),
    path('category/',views.category),
    path('add_category/',views.add_category),
    path('delText/',views.delText),
    path('del_category/',views.del_category),
]
