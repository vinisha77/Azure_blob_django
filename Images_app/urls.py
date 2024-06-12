# urls.py in Images_app directory
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('images/', views.list_images, name='image_list'),  # Update this line
    path('download/<str:filename>/', views.download_file, name='download_file'),
]




