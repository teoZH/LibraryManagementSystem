from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path('make-offer/', views.CreateBookView.as_view(), name='create'),
    path('details/<int:pk>/<str:book_title>/', views.DetailBookView.as_view(), name='details'),
    #path('edit/<int:book_id>/<str:book_title>/', views.edit, name='edit'),
    path('edit/<int:pk>/<str:book_title>/', views.UpdateBookView.as_view(), name='edit'),
    path('delete/<int:book_id>/<str:book_title>/', views.delete, name='delete')
]
