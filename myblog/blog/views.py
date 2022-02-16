from django.shortcuts import render
from blog.models import Users
# Create your views here.
def mainpage(request):
    return render(request,'mainpage.html')

def index(request):
    list=Users.objects.all()
    context={"articles":list}
    return render(request,"index.html",context)

def addpage(request):
    try:
        ob=Users
        ob.title=request.POST['title']
        ob.author=request.POST['author']
        ob.content=request.POST['content']
        ob.save()
        context={'info':'添加成功'}
    except:
        context={'info':'添加失败'}
    return render(request,"info.html",context)

def editpage(request,uid):
    try:
        ob=Users.objects.get(id=uid)
        context={'article':ob}
        return render(request,'edit.html',context)
    except:
        context={'info':'未能找到要修改的信息'}
        return render(request,"info.html",context)

def delete(request,uid):
    try:
        ob=Users.objects.get(id=uid)
        ob.delete()
        context={'info':'删除成功!'}
    except:
        context={'info':'删除失败!'}
    return render(request,"info.html",context)

def update(request):
    try:
        ob=Users.objects.get(id=request.POST['id'])
        ob.title=request.POST['title']
        ob.content=request.POST['content']
        ob.save()
        context={"info":"操作成功"}
    except:
        context={"info":"操作失败"}
    return render(request,"info.html",context)