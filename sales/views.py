from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .forms import ProductForm
from django.contrib import messages


from .models import Product


# Create your views here.

class IndexView(View):
    def get(self, request):
        context = {'product_list': Product.objects.all()}
        return render(request, "index.html", context)


def products(request):
    productsb = Product.objects.all()
    return render(request, "product.html", {'products': productsb})


class ItemView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        context = {'pk': pk, 'product': product}
        return render(request, 'item.html', context)

#complete this part
# def add_to_cart(request, slug):
#     item = get_object_or_404(Product, slug)
#     order_item = OrderItem.objects.create(item=item)
#     order_qs = Order.objects.filter(user=request.user, is_ordered=False)
#     #if order_qs.exists


class addProductView(View):
    def get(self, request):
        form = ProductForm()
        context = {"form": form}
        return render(request, 'addProduct.html', context)

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        context = {
            "form": form
        }
        if form.is_valid():
            messages.success(request, 'Your product has been added successfully!')
            form.save()
            return redirect('/editproducts')



        return render(request, 'addProduct.html', context)

def unlist(request, pk):
    product = Product.objects.get(id=pk)
    product.is_active = False
    product.save()
    return redirect('/editproducts')



def list(request, pk):
    product = Product.objects.get(id=pk)
    product.is_active = True
    product.save()
    return redirect('/editproducts')


def updateProduct(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/editproducts')

    context = {
        "form":form
    }

    return render(request, 'updateProduct.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    #product.delete()
    return render(request, "messages.html", {'product': product})

def deleteItem(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('/')

def editProduct(request):
    productsb = Product.objects.all()
    return render(request, "editproducts.html", {'products': productsb})






