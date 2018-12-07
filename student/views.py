from django.shortcuts import render
from student import models
import requests
# Create your views here.
def main(request):
    return render(request,'main.html',{})
def reg(request):
    return render(request,'reg.html',{})
def user(request):
    if request.method=='POST':
        name = request.POST['name']
        pwd = request.POST['pwd']
        models.UserInfo.objects.create(
            uname=name,
            pwd=pwd
        )
        info_list = models.UserInfo.objects.all()
        print(info_list)
        return render(request,'regsuc.html',{'info_list':info_list})
    else:
        er = 'error'
        return render(request,'main.html',{'notfound':er})
def user_check(request):
    if request.method == 'POST':
        name = request.POST['name']
        pwd = request.POST['pwd']
        try:
            user = models.UserInfo.objects.get(uname=name)
        except:
            return render(request,'fail.html')
        if user.pwd == pwd:
            return render(request,'success.html')
    return render(request,'fail.html')

def stu(request):
    stu = models.StuInfo.objects.all()[:10]
    return render(request, 'stu.html', {'stu': stu})
def stu1(request):
    stu = models.StuInfo.objects.all()[10:20]
    return render(request, 'stu.html', {'stu': stu})
def stu2(request):
    stu = models.StuInfo.objects.all()[20:30]
    return render(request, 'stu.html', {'stu': stu})
def stu3(request):
    stu = models.StuInfo.objects.all()[30:40]
    return render(request, 'stu.html', {'stu': stu})
def stu4(request):
    stu = models.StuInfo.objects.all()[40:50]
    return render(request, 'stu.html', {'stu': stu})


def query(request):
    return render(request,'query.html')
def delete(request):
    return render(request,'delete.html')
def query2(request):
    if request.method=='POST':
        name = request.POST['name']
        stu = models.StuInfo.objects.get(name=name)
        return render(request, 'stu_query.html',{'i':stu})
    else:
        er = 'error'
        print(er)
        return render(request,'stu.html')
def delete2(request):
    if request.method=='POST':
        name = request.POST['name']
        stu = models.StuInfo.objects.get(name=name)
        stu.delete()
        return render(request, 'delsuc.html')
    else:
        er = 'error'
        print(er)
        return render(request,'stu.html')
def delete3(request):
    stu = models.StuInfo.objects.all()
    stu.delete()
    return render(request, 'delsuc.html')


def insert(request):
    return render(request,'insert.html')
def insert2(request):
    if request.method=='POST':
        name = request.POST['name']
        gender = request.POST['gender']
        sno = request.POST['sno']
        score = request.POST['score']
        models.StuInfo.objects.create(
            name=name,
            gender=gender,
            sno=sno,
            score=score,
        )
        return render(request,'inssuc.html')
    else:
        er = 'error'
        return render(request,'stu.html')


def mod(request):
    return render(request, 'mod.html')


def mod2(request):
    if request.method == 'POST':
        name = request.POST['name']
        score = request.POST['score']
        a=models.StuInfo.objects.get(name=name)
        a.score=score
        a.save()
        return render(request, 'updsuc.html')
    else:
        er = 'error'
        return render(request, 'stu.html')






