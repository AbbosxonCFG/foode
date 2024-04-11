from django.shortcuts import render,redirect
from api.models import *


def index(request):
    return render(request,'index.html')







def category_client(request,id):
    category=Category.objects.all()
    stol=Stol.objects.get(id=id)

    contex={
        'category':category,
        'stol_id':id,   
        'stol':stol
        
    }
    
    return render(request,'category_client.html',contex)





def product_detail_client(request,id,pk):
    category=Category.objects.get(id=pk)
    product=category.product.all()
    stol=Stol.objects.get(id=id)
    cart=stol.cart.all()



   

      
    contex={
        "category":category,
        "product":product,
        'stol_id':id,
        'stol':stol,
        'cart':cart,

       
    }
    return render (request,"product_detail_client.html",contex)





def create_cart(request,id,pk):
    stol=Stol.objects.get(id=id)
    product=Product.objects.get(id=pk)
    quantity=1
    exist_cart=Cart.objects.filter(stol=stol,product=product)
    price=product.price

    if not exist_cart.exists():
    
        cart=Cart.objects.create(
            product=product,
            stol=stol,
            quantity=quantity,
            price=price
        )
        
    else:
        exist_cart=exist_cart.first()
        exist_cart.quantity+=1
        exist_cart.price=exist_cart.price+price
        exist_cart.save()

   

    product.quantity=product.quantity-quantity
    product.save()    
    
    return redirect('product_detail_client', id=id, pk=product.category.id)




def reduce_cart(request,id,pk):
    stol=Stol.objects.get(id=id)
    product=Product.objects.get(id=pk)
    price=product.price

    exist_cart=Cart.objects.filter(stol=stol,product=product)
    if exist_cart.exists():
        exist_cart=exist_cart[0]
        exist_cart.quantity-=1
        exist_cart.price=exist_cart.price-price
        exist_cart.save()

        if exist_cart.quantity == 0:
            exist_cart.delete()
        product.quantity+=1
        product.save()

    return redirect('product_detail_client', id=id, pk=product.category.id)




def get_cart(request,id):
    stol=Stol.objects.get(id=id)
    carts=stol.cart.all()
    total_price=0

    for i in carts:
        total_price+=i.price
     

    contex={
        'carts':carts,
        'stol_id':id,
        "stol":stol,
        'total_price':total_price
    }

    return render(request,'cart.html',contex)





def test(request,id):
    stol=Stol.objects.get(id=id)

    contex={
        'stol':stol,
        "stol_id":id
    }

    return render(request,'test.html',contex)


def del_cart(request,id):
    my_list=[]
    stol=Stol.objects.get(id=id)
    carts=stol.cart.all()
    carts.delete()
 
    for i in carts:
        my_list.append(i)
    print(my_list)

    return redirect('test', id=id)




def del_cart_pk(request,id,pk):
    stol=Stol.objects.get(id=id)
    product=Product.objects.get(id=pk)


    exist_cart=Cart.objects.filter(stol=stol,product=product).first()
    if exist_cart:
        
        product.quantity=product.quantity+exist_cart.quantity
        product.save()
        exist_cart.delete()
        return redirect('get_cart',id=id)




def about_us(request):
    info=AboutUs.objects.all()
    contex={
        "info":info
    }
    return render(request,"info.html",contex)














































# def create_order(request):
#     if request.method == 'POST':
#         try:
#             stol_id = request.POST.get('stol_id')
#             product_name = request.POST.get('product_name')
#             quantity = request.POST.get('quantity')
#             product = Product.objects.get(name=product_name)

#             order = Order.objects.create(
#                 stol_id=stol_id,
#                 product=product,
#                 quantity=quantity
#             )
#             product.quantity = product.quantity - int(quantity)
#             product.save()

#             cart = Cart.objects.filter(stol_id=stol_id, is_active=True).first()  # Get the first cart if it exists
#             if cart:
#                 cart.products.add(product)
#             else:
#                 waiters = Waiter.objects.all()
#                 if waiters.exists():  
#                     waiter = waiters.first()  
#                     for i in waiters[1:]:  
#                         if waiter.active_carts_count() > i.active_carts_count():
#                             waiter = i
#                 else:
#                     waiter = None  
#                 cart = Cart.objects.create(
#                     stol_id=stol_id,
#                     waiter=waiter
#                 )
#                 cart.products.add(product)

#             return redirect('category_client')

#         except Exception as e:
#             print(f"Xatolik yuz berdi: {e}")
            
    
#     products = Product.objects.all()
#     stols = Stol.objects.all()
#     return render(request, "order.html", {"products": products, "stols": stols})
