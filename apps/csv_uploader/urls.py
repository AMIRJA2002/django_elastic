from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.UploadCSV.as_view()),
    path('search/', views.Search.as_view()),
    path('delete/<int:id>/', views.ProductDelete.as_view()),
    path('update/<int:id>/', views.ProductUpdate.as_view()),
    path('get/<int:id>/', views.ProductDetail.as_view()),
]
