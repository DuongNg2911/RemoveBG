from django.urls import path

from . import views 

urlpatterns = [
    path('get_image_by_topic/<str:content>/', views.get_image_by_topic),
    path('get_image_by_popular/', views.get_image_by_popular),
    path('upload_file/', views.MyUploadView.as_view()),
] 

