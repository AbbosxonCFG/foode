from django.shortcuts import render,redirect
from api.models import *


def index(request):
    return render(request,'index.html')





def category_client(request):
    category=Category.objects.all()

    contex={
        'category':category,
        
    }
    return render(request,'category_client.html',contex)


def product_detail_client(request,pk):
    category=Category.objects.get(id=pk)
    product=category.product.all()
    

    contex={
        "category":category,
        "product":product,
       
    }
    return render (request,"product_detail_client.html",contex)


# def create_order(request):
#     if request.method=='POST':
#         stol_id=request.POST.get('stol_id')
#         # product_id=request.POST.get('product_id')
#         product_name=request.POST.get('product_name')
#         quantity=request.POST.get('quantity')
#         product=Product.objects.get(name=product_name)

#         order=Order.objects.create(
#             stol_id=stol_id,
#             product=product,
#             quantity=quantity
#         )
#         product=Product.objects.get(name=product_name)
#         product.quantity=product.quantity-int(quantity)
#         product.save()

#         cart=Cart.objects.filter(stol_id=stol_id,is_active=True)
#         if cart.exists():
#             cart[0].products.add(product)
#         else:
#             waiters=Waiter.objects.all()
#             waiter=waiters[0]
#             for i in waiters:
#                 if waiter.active_carts_count()>i.active_carts_count():
#                     waiter=i
#             cart=Cart.objects.create(
#                 stol_id=stol_id,
#                 waiter=waiter
#             )
#             cart.products.add(product)
#             cart.save()


#         return redirect('category_client')
#     products=Product.objects.all()
#     stols=Stol.objects.all()
#     return render(request,"order.html", {"products":products,"stols":stols})

def create_order(request):
    if request.method == 'POST':
        try:
            stol_id = request.POST.get('stol_id')
            product_name = request.POST.get('product_name')
            quantity = request.POST.get('quantity')
            product = Product.objects.get(name=product_name)

            order = Order.objects.create(
                stol_id=stol_id,
                product=product,
                quantity=quantity
            )
            product.quantity = product.quantity - int(quantity)
            product.save()

            cart = Cart.objects.filter(stol_id=stol_id, is_active=True).first()  # Get the first cart if it exists
            if cart:
                cart.products.add(product)
            else:
                waiters = Waiter.objects.all()
                if waiters.exists():  
                    waiter = waiters.first()  
                    for i in waiters[1:]:  
                        if waiter.active_carts_count() > i.active_carts_count():
                            waiter = i
                else:
                    waiter = None  
                cart = Cart.objects.create(
                    stol_id=stol_id,
                    waiter=waiter
                )
                cart.products.add(product)

            return redirect('category_client')

        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
    
    products = Product.objects.all()
    stols = Stol.objects.all()
    return render(request, "order.html", {"products": products, "stols": stols})




def about_us(request):
    info=AboutUs.objects.all()
    contex={
        "info":info
    }
    return render(request,"info.html",contex)







