from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user/', include([
         path('detail/<int:pk>/', views.UserDetailView.as_view(), name="user_detail"),
         path('add/<int:pk>/', views.add_friend, name="friend_add"),
         path('remove/<int:pk>/', views.remove_friend, name="friend_remove"),
         ])),
]
