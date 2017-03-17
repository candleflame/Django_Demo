# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# 第一个参数必须为request，与网页发来的请求有关，request 变量里面包含get或post的内容，用户浏览器，系统等信息在里面
def index1(request):
    # HttpRequest 用来像网页返回内容 类似 print 将内容显示到网页上
    return HttpResponse("Hello world")

# 计算加法
def index2(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(c)


def index3(request):
    return render(request, 'home.html')


def add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))

def home(request):
    """
    传递参数
    :param request:
    :return:
    """
    string="Hello world ！！！"
    """
    传递多个参数
    """
    TutorialList=["Html","css","jquery","Python","Django"]

    """
    显示字典内容
    """
    info_dict={'OS':'windows','author':'admin'}

    """
    条件判断
    """
    List=map(str,range(100))
    return render(request,'home.html',{'string':string,"TutorialList":TutorialList,'info_dict':info_dict,'List':List})