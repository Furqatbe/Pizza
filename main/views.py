from itertools import product
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import viewsets , filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from datetime  import datetime
# Create your views here.


@api_view(['GET'])
def GetSlider(request):
    a = Slider.objects.all().order_by('-id')[0:3]
    ser = SliderSerializer(a , many= True)

    return Response(ser.data)


@api_view(['GET'])
def GetInfo(request):
    a = Info.objects.last()
    ser = InfoSerializer(a)

    return Response(ser.data)


@api_view(['GET'])
def GetWelcome(request):
    a = Welcome_text.objects.last()
    ser = Welcome_textSerializer(a)

    return Response(ser.data)




@api_view(['GET'])
def GetService(request):
    a = Service.objects.all().order_by('-id')[0:3]
    ser =ServiceSerializer(a , many= True)

    return Response(ser.data)

@api_view(['GET'])
def GetProductHots(request):
    a = Product.objects.filter(category__name= 'Pizza').order_by('-id')[0:6]
    ser =ProductSerializer(a , many= True)

    return Response(ser.data)

@api_view(['GET'])
def GetPricing(request):
    a = Product.objects.filter(category__name = 'Pizza', price__gte = 19, price__lte = 50).order_by('-id')[0:8]
    ser =ProductSerializer(a, many=True)

    return Response(ser.data)

@api_view(['GET'])
def GetAchievment(request):
    a =Achievment.objects.all().order_by('-id')[0:4]
    ser = AchievmentSerializer(a , many= True)

    return Response(ser.data)

@api_view(['GET'])
def GetFlCategory(request):
    types = request.GET['type']
    a = Product.objects.filter(category__name= types)
    ser = ProductSerializer(a, many = True)

    return Response(ser.data)

@api_view(['GET'])
def GetBlog(request):
    a = Blog.objects.all()
    ser = BlogSerializer(a, many = True)

    return Response(ser.data)


@api_view(['GET'])
def GetFlBlog(request):
    types = request.GET['type']
    a = Blog.objects.filter(category__name= types)
    ser = BlogSerializer(a, many = True)

    return Response(ser.data)

@api_view(['POST'])
def CreateContact(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    massege = request.POST.get('massage')
    a = Contact.objects.create(first_name = first_name, last_name = last_name, massege = massege)
    ser = ContactSerializer(a)

    return Response(ser.data)


@api_view(['POST'])
def Register(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = User.objects.create_user(username='user-'+username)
    user.set_password(password)
    user.save()
    token = Token.objects.create(user=user)
    DATA = {
        "username":username,
        "password":user.password,
        "token":str(token)

    }
    return Response(DATA)



@api_view(['POST'])
def Login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = User.objects.filter(username='user-'+username)
    if len(user)>0:
        if user[0].check_password(password) == True:
            token = Token.objects.get(user= user[0])
            DATA = {
                    "username":username,
                    "password":user[0].password,
                    "token":str(token)

                }
                
            return Response(DATA)
        else:
            return Response({"status" : "password xato"})
    else:
        return Response({"status" : "username xato"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def AddCart(request):
    product_id = request.POST.get('product')
    product = Product.objects.get(id = product_id)
    user = request.user
    a = Cart.objects.create(product = product, user = user)
    ser = CartSerializer(a)

    return Response(ser.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def DeleteCart(request):
    cart_id = request.POST.get('id')
    user = request.user
    a = Cart.objects.get(id = cart_id, user = user)
    a.delete()
    # ser = CartSerializer(a)


    return Response({'status':"o'cirildi"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def GetCart(request):
    user = request.user
    Carts  = Cart.objects.filter(user = user)
    ser = CartSerializer(Carts, many = True)

    return Response(ser.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def AddOrder(request):
    n = []
    user = request.user
    Carts = Cart.objects.filter(user = user)
    for i in Carts:
        a = Order.objects.create(user = user, product = i.product, price = i.product.price, date = datetime.today())
        n.append(a)
        i.delete()
    ser = OrderSerializer(n, many = True)

    return Response(ser.data)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# def GetOrder(request):
#     user = request.user
#     a = Order.odjects.filter(user = user)
#     ser = OrderSerializer(a, many= True)

#     return Response(ser.data)