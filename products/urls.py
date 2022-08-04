from django.urls import path
from .import views 


urlpatterns = [
    path('', views.ProductDetailsTables.as_view()),
    path('update/<int:productId>',views.ProductsDetailsTablesUpdate.as_view()),
    path('delete/<int:productId>',views.ProductsDetailsTablesDelete.as_view())
]