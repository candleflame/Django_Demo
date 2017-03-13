# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# 第一个参数必须为request，与网页发来的请求有关，request 变量里面包含get或post的内容，用户浏览器，系统等信息在里面
def index1(request):
    # HttpRequest 用来像网页返回内容 类似 print 将内容显示到网页上
    return HttpResponse("Hello world")

def index2(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(c)