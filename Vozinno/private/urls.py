
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from private.views import createemail, editmail, deletemail, createdetails, detailsview, detailsedit, detailsdelete, \
    loginpage, Register, index, logOut

urlpatterns = [
    path("1/", lambda request: render(request, "private/base.html")),
    path ("2", lambda request: render(request, "private/unbase.html")),
    path('createemail/',createemail,name="createemail"),
    path('editmail<int:pk>/',editmail,name="editmail"),
    path('deletemail<int:pk>/',deletemail,name="deletemail"),
    path('createdetails/',createdetails,name="createdetails"),
    path('detailsview<int:pk>/',detailsview,name="detailsview"),
    path('editdetails<int:pk>/',detailsedit,name="detailsedit"),
    path('detailsdelete<int:pk>/',detailsdelete,name="detailsdelete"),
    path('loginpage/', loginpage, name='loginpage'),
    path('register/', Register, name='register'),
    path('', index, name="index"),
    path('logOut',logOut,name='logout')
]
