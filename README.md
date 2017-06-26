## 1，定义
> 在Django中，将前端的内容定义在模板中，然后再把模板交给视图调用，各种漂亮、炫酷的效果就出现了。

## 2,创建模板

为应用booktest下的视图index创建模板index.html，目录结构如下图：
 
 ![这里写图片描述](http://img.blog.csdn.net/20170626225843600?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

设置查找模板的路径：打开test1/settings.py文件，设置TEMPLATES的DIRS值

> 'DIRS': [os.path.join(BASE_DIR, 'templates')],

![这里写图片描述](http://img.blog.csdn.net/20170626230157884?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

##3,定义模板

打开templtes/booktest/index.html文件，在里面写模板代码

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试模板</title>
</head>
<body>
<h1>我是测试模板文件</h1><br/>
模板变量：{{content}}<br/>
使用列表：{{list}}<br/>
<ul>
    {% for i in list%}
    <li>{{i}}</li>
    {% endfor %}
</ul>
</body>
</html>
```

##4，视图调用模板

调用模板分为三步骤：

+ 1.找到模板
+ 2.定义上下文
+ 3.渲染模板
打开booktest/views.py文件，调用上面定义的模板文件


```
from django.http import HttpResponse
from django.template import loader,RequestContext

def index(request):
    # 1.获取模板
    template=loader.get_template('booktest/index.html')
    # 2.定义上下文
    context=RequestContext(request,{'content':'hello python','list':range(0,6)})
    # 3.渲染模板
    return HttpResponse(template.render(context))

```

![这里写图片描述](http://img.blog.csdn.net/20170627000600287?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


##5,视图调用模板简写（推荐这种）

视图调用模板都要执行以上三部分，于是Django提供了一个函数render封装了以上代码。 方法render包含3个参数：

第一个参数为request对象
第二个参数为模板文件路径
第三个参数为字典，表示向模板中传递的上下文数据
打开booktest/views.py文件，调用render的代码如下：

```

from django.shortcuts import render

def index(request):
    context={'content':'hello python','list':range(0,6)}
    return render(request,'booktest/index.html',context)
```


