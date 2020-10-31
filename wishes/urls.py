from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('wish_list/', views.wish_list, name="wish_list"),
    path('waiting/', views.waiting, name="waiting"),
    path('<int:pk>/', views.wish_detail, name="wish_detail"),
    path('<int:pk>/reply', views.reply, name="reply"),
    path('gallery', views.gallery, name="gallery"),
]