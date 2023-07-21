from django.urls import path, include

from petstagram_try.photos import views

urlpatterns = (
    path('add/', views.PhotoAddView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', views.details_photo, name='details-photo'),
        path('edit/', views.edit_photo, name='edit-photo'),
        path('delete/', views.delete_photo, name='delete-photo'),
    ])),
)
