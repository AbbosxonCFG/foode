from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view ,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import BasicAuthentication,SessionAuthentication

from .permissions import IsAdmin
from rest_framework.views import APIView
# import qrcode

#!--------------------------------------------------------QR CODE--------------------------------------------#



# class QRCodeGenerator(APIView):
#     def get(self, request):
#         qr_code_data = []
#         base_url = "http://127.0.0.1:8000/api/category_list/"  # Sizning saytingiz URL manzili
#         for i in range(1, 11):
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_L,
#                 box_size=10,
#                 border=4,
#             )
#             qr.add_data(base_url + str(i))  # Saytingiz URL'si va sonni birlashtiramiz
#             qr.make(fit=True)

#             img = qr.make_image(fill_color="black", back_color="white")
#             qr_code_name = f"qr_code_{i}.png"
#             img.save(qr_code_name)
#             qr_code_data.append({"number": i, "qr_code": qr_code_name, "url": base_url + str(i)})  # Ma'lumotlarni qo'shamiz

#         return Response(qr_code_data, status=status.HTTP_200_OK)


#!--------------------------------------------CATEGORY---------------------------------------------------#



@api_view(['GET'])
def category_list_pk(request):
    pk=request.GET.get('pk')
    if pk is not None:
        category=Category.objects.filter(id=pk)
        if category.exists():
            serializer=CategorySerializer(category)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("There is not category in this id")
    categoryes=Category.objects.all()
    serializer=CategorySerializer(categoryes,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)





@api_view(['PUT','POST','DELETE'])
@permission_classes([IsAdmin])
@authentication_classes([BasicAuthentication])
def category_main(request):
    pk=request.GET.get('pk')
    name=request.data.get('name')
    if request.method=='POST':
        category=Category.objects.create(
            name=name
        )
        serializer=CategorySerializer(category).data
        contex={
            'message':'Category created',
            "data":serializer
        }
        return Response(contex,status=201)
    if request.method=='PUT':
        if pk is not None:
            category=Category.objects.filter(id=pk)
            if category.exists():
                category=category[0]
                if name is not None:category.name=name
                category.save()
                serializer=CategorySerializer(category).data
                contex={
                    "message":"Category updated",
                    "data":serializer
                }
                return Response(contex,status=status.HTTP_201_CREATED)
            else:
                return Response("There is not category in this id",status=404)
        else:
            return Response("You should enter categry's id thah you want to update",status=404)
    if request.method=='DELETE':
        if pk is not None:
            category=Category.objects.filter(id=pk)
            if category.exists():
                category=category[0]
                category.delete()
                return Response("Category deleted",status=200)
            else:
                return Response("There is not category in this id",status=404)
        else:
            return Response("You should enter categry's id thah you want to delete",status=404)
        

#!----------------------------------------PRODUCT------------------------------------------------#


@api_view(['GET'])
def produc_list_pk(request):
    pk=request.GET.get('pk')
    if pk is not None:
        product=Product.objects.filter(id=pk)
        if product.exists():
            product=product[0]
            serializer=ProductSerializer(product)
            return Response(serializer.data,status=200)
        else:
            return Response("There is not such as product")
    product=Product.objects.all()
    serializer=ProductSerializer(product,many=True)
    return Response(serializer.data,status=200)



#!--------------------------------------------------------ORDER---------------------------------------------------#


@api_view(['POST','DELETE'])
def order(request):
    # Request ma'lumotlari
    stol_num = request.data.get('stol_num')
    product_name = request.data.get('product_name')
    quantity = request.data.get('quantity')

    if request.method=='POST':
        if stol_num is not None:
            stol=Stol.objects.filter(num=stol_num)
            if stol.exists():
                stol=stol[0]
            else:
                return Response("There is not such as table",status=404)
        else:
            return Response("This field is required (stol_num)")
        
        if product_name is not None:
            product=Product.objects.filter(name=product_name)
            if product.exists():
                product=product[0]
            else:
                return Response("There is not such as product")
        else:
            return Response("This field is required (product_name)")
        
        if quantity is  None:
            return Response("This field is required (quantity)")
        
        order=Order.objects.filter(stol__num=stol_num,product__name=product_name)
        if not order.exists():

            order=Order.objects.create(
                product=product,
                stol=stol,
                quantity=quantity
            )
            serializer=OrderSerializer(order).data
            contex={
                'message':'Order created',
                'data':serializer
            }
            return Response(data=contex,status=status.HTTP_201_CREATED)
        else:
            return Response("This order already added",status=200)
        
    if request.method=='DELETE':
        if product_name is not None:
            order=Order.objects.filter(product__name=product_name,stol__num=stol_num)
            if order.exists():
                order[0].delete()
                return Response({"message":"Order deleted"},status=200)
            else:
                return Response("There is not such as order",status=404)
        else:
            return Response("You shoul enter the (product_name) and (stol_num) to delete your order ")
        



        



    

   

   




























































#!---------------------REGISTER SERIALIZER-----------------------------
    
class Register(GenericAPIView):
    serializer_class=RegisterSerializer

    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            contex={
                "message":"User has succesfully created",
                "data":serializer.data

                
            }
            return Response(data=contex,status=201)
        return Response(data=serializer.errors,status=400)
    
