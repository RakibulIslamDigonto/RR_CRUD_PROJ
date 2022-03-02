from django.urls import path
from . import views


urlpatterns = [
    path('', views.MyPostListAPI.as_view(), name='posts-list-view'),
    path('create/', views.PostCreateAPI.as_view(), name='create-view'),
    path('details/<int:pk>/', views.MyPostDetailsAPI.as_view(), name='post-detail-view'),

]

