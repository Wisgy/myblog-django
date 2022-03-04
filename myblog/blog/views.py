from django.shortcuts import render
from blog.models import articles,comments
from django.http import HttpResponse
# Create your views here.
def mainpage(request):
    return render(request,'mainpage.html')

def index(request):
    list=articles.objects.all()
    context={"articles":list}
    return render(request,"index.html",context)

def browse(request,uid):
    ob=articles.objects.get(id=uid)
    com=comments.objects.filter(artid=uid)
    context={'article':ob,'comments':com}
    return render(request,"browse.html",context)


def addpage(request,uid):
    ob=articles.objects.get(id=uid)
    return render(request,'add.html',{'article':ob})

def add(request):
    try:
        ob=comments()
        ob.author=request.POST['author']
        ob.content=request.POST['content']
        ob.artid=request.POST['artid']
        ob.save()
        context={'info':'添加成功'}
    except:
        context={'info':'添加失败'}
    return render(request,"info.html",context)

# def delete(request,uid):
#     try:
#         ob=articles.objects.get(id=uid)
#         ob.delete()
#         context={'info':'删除成功!'}
#     except:
#         context={'info':'删除失败!'}
#     return render(request,"info.html",context)

# def update(request):
#     try:
#         ob=articles.objects.get(id=request.POST['id'])
#         ob.title=request.POST['title']
#         ob.content=request.POST['content']
#         ob.save()
#         context={"info":"操作成功"}
#     except:
#         context={"info":"操作失败"}
#     return render(request,"info.html",context)