from django.shortcuts import render

# Create your views here.

#主页
def home(request):
    retuen render(request,'axf/home.html')

#闪送超市
def market(request):
    retuen render(request,'axf/market.html')
    
#购物车
def cart(request):
    retuen render(request,'axf/cart.html')
    
#我的页面
def mine(request):
    retuen render(request,'axf/mine.html')