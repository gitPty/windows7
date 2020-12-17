from django.urls import re_path
from wintel_web import views

urlpatterns = [
    re_path(r'^$', views.Login.as_view()),          # 直接匹配根域名
    re_path(r'^index/$', views.Index.as_view()),
    # re_path(r'^index/$', views.index),
    re_path(r'^logout/$', views.logout),
    
]
