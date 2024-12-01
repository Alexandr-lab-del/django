from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from catalog.models import Product, Category
from catalog.forms import ProductForm
from .services import get_products_by_category, get_products_from_cache


class ProductListView(ListView):

    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return get_products_from_cache()


class HomeView(TemplateView):

    template_name = 'products/home.html'


class ContactsView(TemplateView):

    template_name = 'products/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.change_product'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.has_perm('catalog.delete_product')


@permission_required('catalog.can_unpublish_product', raise_exception=True)
def unpublish_product(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    product.status = 'draft'
    product.save()
    return redirect('catalog:product_list')


@login_required
@permission_required('catalog.delete_product', raise_exception=True)
def delete_product(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    if request.user == product.owner or request.user.has_perm('catalog.delete_product'):
        product.delete()
        return redirect('catalog:product_list')
    else:
        raise PermissionDenied


class ProductsByCategoryView(ListView):
    model = Category

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return get_products_by_category(category_id=category_id)
