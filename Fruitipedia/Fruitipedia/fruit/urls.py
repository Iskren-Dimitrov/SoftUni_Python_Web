from django.urls import path, include

from Fruitipedia.fruit import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # fruit urls
    path('create/', views.fruit_create, name='fruit-create'),
    path('details/<int:pk>/', views.fruit_details, name='fruit-details'),
    path('edit/<int:pk>/', views.fruit_edit, name='fruit-edit'),
    path('delete/<int:pk>/', views.fruit_delete, name='fruit-delete'),

    # profile urls
    path('profile/', include([
        path('create/', views.profile_create, name='profile-create'),
        path('details/', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path('delete/', views.profile_delete, name='profile-delete'),
    ]))
]
