"""
URL configuration for the_cake_fairy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from the_cake_fairy import views
from services.views import signup
from services.views import login


urlpatterns = [
    path('', views.homepage), 
    path('admin/', admin.site.urls),
    path('about/', views.aboutUS),
    path('review/', views.review),
    path('blogs/', views.blogs),
    path('contact/', views.contact),
    path('userform/', views.userform),
    path('submitform/', views.submitform, name='submitform'),
    path('shop/', views.shop),
    path('product/', views.product),
    path('product7/', views.product7),
    path('product1/', views.product1),
    path('product2/', views.product2),
    path('product3/', views.product3),
    path('product4/', views.product4),
    path('product5/', views.product5),
    path('product6/', views.product6),
    path('product8/', views.product8),
    path('', views.payment_details),
    path('payment/', views.payment, name='payment'),
    path('login/', login,name='login'),
    path('signup/', signup)   
]
 