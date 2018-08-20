from django.shortcuts import render
from .models import Wheel, Nav, Mustbuy, Shop,Mainshow


# Create your views here.

# 主页
def home(request):
    title = '主页'
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustBuyList = Mustbuy.objects.all()
    shop1 = Shop.objects.get(id=1)
    shop2 = Shop.objects.all()[1:3]
    shop3 = Shop.objects.all()[3:7]
    shop4 = Shop.objects.all()[7:11]
    mainList = Mainshow.objects.all()

    return render(request, 'axf/home.html', {'title': title, 'wheelsList': wheelsList, 'navList': navList,
                                             'mustBuyList': mustBuyList, 'shop1': shop1, 'shop2': shop2,
                                             'shop3': shop3, 'shop4': shop4,'mainList':mainList,})


# 闪送超市
def market(request):
    title = '闪送超市'
    return render(request, 'axf/market.html', {'title': title})


# 购物车
def cart(request):
    title = '购物车'
    return render(request, 'axf/cart.html', {'title': title})


# 我的页面
def mine(request):
    title = '我的页面'
    return render(request, 'axf/mine.html', {'title': title})
