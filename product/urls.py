from django.urls import path 
from product.views import ProductsView

urlpatterns = [
    path('', ProductsView.as_view())
]