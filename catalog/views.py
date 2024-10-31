from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class HomeView(TemplateView):
    template_name = 'products/home.html'


class ContactsView(TemplateView):
    template_name = 'products/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
