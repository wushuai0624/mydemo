from . import views
from django.urls import path

urlpatterns = [
    path('',views.main,name="main" ),
    path('reg/',views.reg,name="reg" ),
    path('login/',views.main,name="login" ),
    path('user/',views.user,name="user"),
    path('check/',views.user_check,name="check"),
    path('stu/',views.stu,name="stu"),
    path('stu1/',views.stu1,name="stu1"),
    path('stu2/',views.stu2,name="stu2"),
    path('stu3/',views.stu3,name="stu3"),
    path('stu4/',views.stu4,name="stu4"),
    path('query/',views.query,name="query"),
    path('query2/',views.query2,name="query2"),
    path('mod/',views.mod,name="mod"),
    path('mod2/',views.mod2,name="mod2"),
    path('delete/',views.delete,name="delete"),
    path('delete2/',views.delete2,name="delete2"),
    path('delete3/',views.delete3,name="delete3"),
    path('insert/',views.insert,name="insert"),
    path('insert2/',views.insert2,name="insert2"),
]
