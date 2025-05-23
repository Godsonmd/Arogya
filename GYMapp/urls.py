"""
URL configuration for GYM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('fgps/',views.fp,name="fp"),
    path('fgps1/',views.fp1,name="fp1"),
    path('sendmail/',views.send_vemail,name="send_vemail"),
    path('dsendmail/',views.dsend_vemail,name="send_vemail"),
    path('dfgps/',views.dfp,name="dfp"),
    path('dfgps1/',views.dfp1,name="dfp1"),
    path('details/',views.details,name="details"),
    path('details/dboys/',views.dboys,name="dboys"),
    path('details/dgirls/',views.dgirls,name="dgirls"),
    path('details/dboys/boy',views.ddboys,name="ddboys"),
    path('details/dgirls/girl',views.ddgirls,name="ddgirls"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('tc/',views.tc,name="tc"),
    path('purchase/',views.purchase,name="purchase"),
    path('nearest-gyms/', views.find_nearest_gyms, name='find_nearest_gyms'),
    path('chat/', views.gai, name='openai_chat'),
    path('api/gai/', views.gAi_view, name='gAi_view'),
    path('Abot/',views.Bot,name="bot"),
    path('helpers/',views.drform,name="drform"),
    path('drpro/',views.drpro,name="drpro"),
    path('visit/',views.visit,name="visit"),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
]
