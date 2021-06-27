"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from FirstApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('ht/',views.ht),
    path('u/<str:uname>/',views.usernameprint),
    path('us/<str:uname>/<int:age>/',views.us),
    path('emp/<str:eid>/<int:eage>/<str:ename>',views.empdetails),
    path('qw/',views.htm),
    path('yt/<str:uname>/',views.html),
    path('de/<str:uname>/<int:id>/',views.details),
    path('pt/<int:id>/<str:ename>/',views.empname),
    path('stud/',views.studentdetails),
    path('internalJS/',views.internalJS),
    path('myform/',views.myform,name='myform'),
    path('register/',views.reg,name='register'),
    path('login/',views.log,name='login'),
    path('btstrp/',views.bootstrapfun),
    path('btrg/',views.btregi,name="btr"),
    path('reg/',views.reg,name="reg1"),
    path('display/',views.display,name="dt"),
    path('viw/<int:y>/',views.sview,name="sv"),
    path('upu/<int:q>/',views.supt,name="sup"),
    path('snd/<int:p>/',views.sndl,name="del"),
]
