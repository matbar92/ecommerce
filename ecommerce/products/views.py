from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
# Create your views here.
from .models import Product


class HomeView(View):

    def get(self, request):
        template = 'products/home.html'
        ctx = locals()
        return render(request,template,ctx)

class ProductsView(View):

    def get(self,request):
        template = 'products/all.html'
        products = Product.objects.all()
        ctx = {'products': products}
        return render(request, template, ctx)
