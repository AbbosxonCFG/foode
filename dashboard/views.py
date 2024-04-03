import qrcode

from api.serializer import *
from django.shortcuts import render, redirect, get_object_or_404

from api.models import *

def index(request):
    return render(request, 'index_d.html')






def table(request):
    if request.method == 'POST':
        number = request.POST['number']
        table = Stol.objects.create(
            number=number
        )
        table.generate_qr(f'{request.get_host()}/client/{table.number}')
        return redirect('table')  # Redirect to avoid double form submission
    tables = Stol.objects.all()
    return render(request, 'table.html', {'tables': tables})


def table_delete(request,pk):
    stol=Stol.objects.get(id=pk)
    stol.delete()
    return redirect('table')









def product(request):
    products = Product.objects.all().order_by('-id')
    for i in products:
        print(i.name)
    contex = {
        'products': products
    }
    return render(request, 'product.html', contex)



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
        Product.objects.create(
            name=name,
            price=price,
            image=image,
            category_id=category_id,
            quantity=quantity
        )
        return redirect('product')
    category = Category.objects.all()
    return render(request, 'product_add.html', {"category": category})





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




def stol(request):
    stols=Stol.objects.all()
    return render(request,'dashboard_order.html',{'stols':stols})




def order(request,pk):
    stol=Stol.objects.get(id=pk)
    orders=stol.order.all()



    contex={
        "stol":stol,
        "orders":orders
    }
    return render(request,"detail_order.html",contex)




def order_delete(request,pk):
    stol=Stol.objects.get(id=pk)
    carts=stol.carts.all()
    carts.delete()
    order=stol.order.all()
    order.delete()
    return redirect('stol')




def category(request):
    categories=Category.objects.all()
    return render(request,'categories.html',{"categories":categories})




def category_add(request):
    if request.method=='POST':
        name=request.POST.get('name')

        category=Category.objects.create(
            name=name
        )
        return redirect('category')
    return render(request,'category_add.html')



def category_delete(request,pk):
    category=Category.objects.get(id=pk)
    category.delete()
    return redirect('category')



     


