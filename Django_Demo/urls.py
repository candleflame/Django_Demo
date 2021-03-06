# coding:utf-8
"""Django_Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views

# 总的urls的配置文件
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',learn_views.index1), # 输出Helloworld
    url(r'^add/$',learn_views.index2,name='add'), # 计算a和b的加法


    #name 可以用于在 templates, models, views ……中得到对应的网址，相当于“给网址取了个名字”，
    # 只要这个名字不变，网址变了也能通过名字获取到
    # url(r'^$',learn_views.index3, name="home"),
    url(r'^$',learn_views.home, name="home"),
    url(r'^add/(\d+)/(\d+)/$',learn_views.add2,name="add2"),
]
