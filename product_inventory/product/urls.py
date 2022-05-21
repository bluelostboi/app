from django.urls import path
from .views import InventoryView,inventory_search, InventorySearchView,InventoryEditView, DeleteProductView

urlpatterns = [
    path('create/', InventoryView.as_view()),
    path('products/', inventory_search),
    path('products/<product_name>', InventorySearchView.as_view()),
    path('edit/<product_name>/',InventoryEditView.as_view()),
    path('delete/<product_name>/',DeleteProductView.as_view()),
]