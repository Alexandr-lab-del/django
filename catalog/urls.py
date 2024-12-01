from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    ProductListView, ProductDetailView, ProductCreateView,
    ProductUpdateView, ProductDeleteView, HomeView, ContactsView, unpublish_product, ProductsByCategoryView
)

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('home/', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:product_id>/unpublish/', unpublish_product, name='unpublish_product'),
    path('category/<int:pk>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]
