from django.shortcuts import render


# Create your views here.

# 主页
def home(request):
    title = '主页'
    return render(request, 'axf/home.html',{'title':title})


# 闪送超市
def market(request):
    title = '闪送超市'
    return render(request, 'axf/market.html',{'title':title})


# 购物车
def cart(request):
    title = '购物车'
    return render(request, 'axf/cart.html',{'title':title})


# 我的页面
def mine(request):
    title = '我的页面'
    return render(request, 'axf/mine.html',{'title':title})
