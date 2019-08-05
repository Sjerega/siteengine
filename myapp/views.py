from django.views.generic import View
#from django.shortcuts import render, redirect
from .models import Product, Tag
from .utils import *
from .forms import TagForm, ProductForm


def root(request):
    return redirect('myapp/product_list_url')


class ProductsList(ObjectsListMixin, View):
    model = Product
    template = 'myapp/products.html'
    context_key = 'products'


class ProductDetail(ObjectDetailMixin, View):
    model = Product
    template = 'myapp/product.html'


class ProductCreate(ObjectCreateMixin, View):
    form_model = ProductForm
    template = 'myapp/product_create.html'


class ProductUpdate(ObjectUpdateMixin, View):
    model = Product
    form_model = ProductForm
    template = 'myapp/product_update.html'


class TagsList(ObjectsListMixin, View):
    model = Tag
    template = 'myapp/tags.html'
    context_key = 'tags'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'myapp/tag.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'myapp/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'myapp/tag_update.html'
