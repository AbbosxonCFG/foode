from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Category, Product, Order, Cart, Waiter
from api.serializer import CategorySerializer, ProductSerializer, OrderSerializer, CartSerializer


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_products(request):
    category_id = request.GET.get('category_id')
    product_id = request.GET.get('product_id')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    product = Product.objects.get(id=product_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_order(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')
    table_id = request.data.get('table_id')
    order = Order.objects.create(
        product_id=product_id,
        stol_id=table_id,
        quantity=quantity
    )
    product = Product.objects.get(id=product_id)
    product.quantity = int(product.quantity) - int(quantity)
    product.save()
    cart = Cart.objects.filter(stol_id=table_id, is_active=True)
    if cart:
        cart[0].products.add(product)
    else:
        waiters = Waiter.objects.all()
        waiter = waiters[0]
        for i in waiters:
            if waiter.active_carts_count() > i.active_carts_count():
                waiter = i
        cart = Cart.objects.create(
            waiter=waiter,
            stol_id=table_id,
        )
        cart.products.add(product)
    serializer = OrderSerializer(order).data
    contex = {
        "Message": 'Order created',
        'data': serializer

    }
    return Response(contex, status=201)

    
    
    
    # return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)




@api_view(['GET'])
def get_cart(request):
    table_id = request.GET.get('table_id')
    try:
        cart = Cart.objects.get(stol_id=table_id, is_active=True)
        return Response(CartSerializer(cart).data, status=status.HTTP_200_OK)
    except Cart.DoesNotExist as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)












































