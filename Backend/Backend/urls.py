"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from online_shop import views, api_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', api_view.UserViewSet)
router.register(r'groups', api_view.GroupViewSet)
router.register(r'posts', api_view.PostViewSet)
router.register(r'products', api_view.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('', views.home),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts, name='posts'),
    path('create-posts/', views.create_posts, name='create_posts'),
    path('post/<int:pk>/update/', views.update_posts, name='update_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('products/', views.products, name='products' ),
    path('create-product/', views.create_product, name='create_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
]

# cd Backend
# ..\venv\Scripts\python.exe manage.py runserver
