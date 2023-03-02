from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render

from products.forms import ProductForm, VersionForm
from products.models import Product, Version, Category
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from products.services import cache_categories


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super(ProductCreateView, self).form_valid(form)


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user.has_perm('moderator') or product.owner == self.request.user


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()  # Student
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()  # Subject

        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        return self.request.user.has_perm('moderator') or product.owner == self.request.user


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['cache_categories'] = cache_categories()
        return context_data


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('products:category_list')
