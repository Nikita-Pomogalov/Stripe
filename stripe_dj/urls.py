"""
URL configuration for stripe_dj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app_stripe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:id>/', views.detail, name='item_detail'),
    path('buy/<int:id>/', views.create_session_for_item, name='item_buy'),
    path('order/<int:id>/', views.order_detail, name='order_detail'),
    path('order/buy/<int:id>/', views.create_session_for_order, name='order_buy')
]


