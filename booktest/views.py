from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo


# Create your views here.

def index(request):
    return render(request, 'booktest/index.html', {'content':'hello python','list': range(0,6)})


# 首页视图
def first(request):
    # 1，查询所有图书的信息
    books = BookInfo.objects.all()
    # 2,使用模板文件
    return render(request, 'booktest/first.html', {'books': books})


# 详情页视图
def detail(request, bid):  # bid代码点击的图书的id
    # 1,查询某一本图书
    book = BookInfo.objects.get(id=int(bid))
    # 2,根据查到的书，找到书中所有的英雄
    heros = book.heroinfo_set.all()
    # 3,使用模板文件
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})

# 以下为原生模板步骤
# 1.加载模板文件,返回一个模板对象
# temp = loader.get_template('booktest/index2.html')
# 2.定义模板上下文：传递数据
# context = RequestContext(request, {})
# 3.模板渲染:得到标准的html内容
# res_html = temp.render(context)
# 4.返回内容给浏览器
# return HttpResponse(res_html)
