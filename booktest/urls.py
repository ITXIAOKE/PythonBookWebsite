from django.conf.urls import url
from . import views

urlpatterns=[
    # 测试
    url(r'^index/$',views.index),
    # 首页url
    url(r'^first/$',views.first),
    # 详情页url
    url(r'^(\d+)/$',views.detail)
]