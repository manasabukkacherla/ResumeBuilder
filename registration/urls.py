"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.FrontPage,name='frontpage'),
    path('home/',views.HomePage,name='home'),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('resume/',views.ResumePage,name='resume'),
    path('templet2/',views.TempletPage2,name='templet2'),
    path('templet3/',views.TempletPage3,name='templet3'),
    path('templetespage/',views.TempletPage,name='templetespage'),
    path('templete4/',views.TempletPage4,name='templete4'),
    path('t5/',views.TempletPage5,name='t5'),
    path('t6/',views.TempletPage6,name='t6'),
    
    
]
