from django.urls import path

from petstagram.photos import views

urlpatterns = [
    path('add', views.photo_add_page, name='photo_add'),
    path('<int:pk>', views.photo_details_page, name='photo_details'),
    path('<int:pk>/edit', views.photo_edit_page, name='photo_edit'),
]