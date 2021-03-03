"""custorder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from ordercust import views
import ordercust



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('signin', views.UserLoginView),
    path('admin/', admin.site.urls),
    path('orders/',views.order_list),
    path('customer/', views.customer_list),
    path('customers/', views.customer_detail),
    # path('customers/name$', views.customer_list_name),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('social/auth/', views.social_login),
   
]