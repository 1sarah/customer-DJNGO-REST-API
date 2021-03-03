from django.shortcuts import render

# Create your views here.
from ordercust.models import Customer, Order, User
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions, status
from .serializers import CustomerSerializer, OrderSerializer, SocialAuthSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from unicodedata import name

from social_django.utils import load_backend, load_strategy
from social_core.backends.oauth import BaseOAuth1, BaseOAuth2
from social_core.exceptions import MissingBackend


# class CustomerViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows customers to be viewed or edited.
#     """
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class OrderViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows orders to be viewed or edited.
#     """
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'POST', 'DELETE'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            customers = customers.filter(title__icontains=name)
        
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Customer.objects.all().delete()
        return JsonResponse({'message': '{} Customers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request):
    name = request.GET.get("name")
    # import pdb;pdb.set_trace()
    try: 
        customer = Customer.objects.get(name=name) 
    except Customer.DoesNotExist: 
        return JsonResponse({'message': 'The customer does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        customer_serializer = CustomerSerializer(customer)        
        return JsonResponse(customer_serializer.data) 
 
    elif request.method == 'PUT': 
        customer_data = JSONParser().parse(request) 
        customer_serializer = CustomerSerializer(customer, data=customer_data) 
        if customer_serializer.is_valid(): 
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        customer.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def customer_list_name(request):
    customers = Customer.objects.filter(name=name)
        
    if request.method == 'GET': 
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            orders = orders.filter(title__icontains=name)
        
        orders_serializer = OrderSerializer(orders, many=True)
        return JsonResponse(orders_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse(order_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Order.objects.all().delete()
        return JsonResponse({'message': '{} orders were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
      

@api_view(['POST'])
def social_login(request):
    serializer_class = SocialAuthSerializer
    serializer = serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    authenticated_user = request.user if not request.user.is_anonymous else None
    provider = serializer.data.get('provider')
    strategy = load_strategy(request)
    try:
        backend = load_backend(
            strategy=strategy, name=provider, redirect_uri=None)
    except MissingBackend:
        return JsonResponse({"error": "Provider invalid or not supported"},
                        status=status.HTTP_404_NOT_FOUND)
    if isinstance(backend, BaseOAuth1):
        token = {
            'oauth_token': serializer.data.get('access_token'),
            'oauth_token_secret': serializer.data.get('access_token_secret')
        }
    elif isinstance(backend, BaseOAuth2):
        token = serializer.data.get('access_token')
    try:
        user = backend.do_auth(token, user=authenticated_user)
    except BaseException as e:
        return JsonResponse({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    if user:
        user.is_verified = True
        # user.token = functionto generate token
        user.save()
        serializer = UserSerializer(user)
        serializer.instance = user
        
        import pdb;pdb.set_trace()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)



