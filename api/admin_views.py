from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Waiter, Stol
from api.serializer import WaiterSerializer, StolSerializer


@api_view(['POST'])
def create_waiter(request):
    name = request.data.get('name')
    waiter = Waiter.objects.create(name=name)
    return Response(WaiterSerializer(waiter).data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_table(request):
    number = request.data.get('number')
    stol = Stol.objects.create(number=number)
    return Response(StolSerializer(stol).data, status=status.HTTP_201_CREATED)


@api_view([''])





































