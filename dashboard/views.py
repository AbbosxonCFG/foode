from django.shortcuts import render,redirect
from api.models import *
from rest_framework .decorators import *
from rest_framework.response import Response
from rest_framework import status
from api.serializer import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404



def index(request):
    return render(request, 'index.html')



def table(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
    return render(request, 'table.html')



def product(request):
    products=Product.objects.all().order_by('-id')
    for i in products:
        print(i.name)
    contex={
        'products':products
    }
    return render(request,'product.html',contex)



def product_detail(request,pk):
    product=Product.objects.get(id=pk)
    contex={
        'product':product
    }
    return render(request,'product_detail.html',contex)



def product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category_id = request.POST.get('category_id')
        quantity = request.POST.get('quantity')

        if name and price and category_id and quantity:
            product = Product.objects.create(
                name=name,
                price=price,
                image=image,
                category_id=category_id,
                quantity=quantity,
            )
            messages.success(request,'Product added successfully')
            return redirect('product') 
        else:
            messages.error(request,"You shuuld fill all the fields")
            return render(request, 'product_add.html')
    else:
        return render(request, 'product_add.html')





def product_edit(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category_id = request.POST.get('category_id')
        quantity = request.POST.get('quantity')

        if name and price and category_id and quantity:
            product.name = name
            product.price = price
            product.category_id = category_id
            product.quantity = quantity
            if image:
                product.image = image

            product.save()

            messages.success(request, 'Product updated successfully')
            return redirect('product')
        else:
            messages.error(request, "You should fill all the fields")
            return render(request, 'product_edit.html', {'product': product})
    else:
        return render(request, 'product_edit.html', {'product': product})





def product_delete(request,pk):
    product=Product.objects.get(id=pk)
    order=Order.objects.filter(product__id=pk)
    order.delete()
    order.delete()
    product.delete()
    return redirect('product')


     


