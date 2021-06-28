import json

from django.forms import modelform_factory
from django.shortcuts import render, redirect


# Create your views here.
from content.models import content, categorys
from user.models import User


def index(request):
    # if request.COOKIES.get("is_login"):
    #     return render(request,'index.html',locals())
    return render(request,'index.html',locals())


def HomePage(request):
    if request.COOKIES.get("user_name") is None:
        return redirect("/login/")
    #获取分类id
    article_type = request.GET.get('id',1)
    article_type=categorys.objects.get(id=article_type)
    items=article_type.content_set.all()
    return render(request,'blog.html',locals())


def loginOut(request):
    resp=redirect("/login/")
    resp.set_cookie("is_login",value=False)
    return resp

def editor(request):
    if request.COOKIES.get("user_name") is None:
        return redirect("/login/")
    try:
        #接受从detail页面传过来的文章id
        # 如果存在则代表是重新编辑，否则为HomePage页面创建一个新页面
        id = request.GET.get('id')
        context = content.objects.get(id=id)
    except:
        context=''
    ### 这里是分类页面取数据显示逻辑
    if request.method=="POST":
        #如果context不为空则则表示为文章重新编辑
        if context:
            # 将context值如果改动则获取改动,若未改动将其设置为原值
            title = request.POST.get('title', context.title)
            text_type = request.POST.get('text_type', context.select)
            descHtml = request.POST.get('descHtml', context.descHtml)
            descMd = request.POST.get('descMd', context.descMd)
            items=context
        #如果为空则表示第一次创建文档
        else:
            # 获取网页输入的值
            title = request.POST.get('title', '')
            text_type = request.POST.get('text_type', '')
            descHtml = request.POST.get('descHtml', '')
            descMd = request.POST.get('descMd', '')
            items = content()
        user=User.objects.get(name=request.COOKIES.get("user_name", ''))
        items.select= categorys.objects.get(category=text_type,user_name=user)
        items.title = title
        items.descHtml = descHtml
        items.descMd=descMd
        items.save()
        return redirect("/content/HomePage/?id="+str(items.select.id))
    article_type=request.GET.get('article_type')
    print(article_type)
    article_type=categorys.objects.get(id=article_type)
    # 从数据库取所有关联Uesr的分类
    user_name = request.COOKIES.get("user_name", '')
    # 获取数据库中该用户的对象
    user=User.objects.get(name=user_name)
    text_types=user.categorys_set.all()
    return render(request,'MarkdownEditor.html',locals())

def reEditor(request):
    id = request.GET.get('id', 1)
    try:
        context = content.objects.get(id=id)
        print(context.descMd)
    except:
        return render(request,'test.html',locals())
    return render(request,'MarkdownEditor.html',locals())
#详情页
def detail(request):
    if request.COOKIES.get("user_name") is None:
        return redirect("/login/")
    #获取分类id
    id=request.GET.get('id', 1)
    try:
        #获取文章内容
        context=content.objects.get(id=id)
    except:
        return redirect("/content/test/")
    return render(request,'detail.html',locals())


def test(request):
    return render(request,"test.html",locals())


def delText(request):
    #获取被删除文章id
    id = request.GET.get('id', 1)
    try:
        context = content.objects.get(id=id)
        article_id=categorys.objects.get(category=context.select)
    except:
        context = ''

    content.delete(context)
    return redirect("/content/HomePage/?id="+str(article_id.id))


def category(request):
    if request.COOKIES.get("user_name") is None:
        return redirect("/login/")
    # if request=="POST":
    #从数据库取所有关联Uesr的分类
    user_name=request.COOKIES.get("user_name",'')
    #获取数据库中该用户的对象
    user=User.objects.get(name=user_name)
    fileForm = modelform_factory(categorys, fields=['category', 'cate_img'])
    form = fileForm(request.POST, request.FILES)
    article_type = user.categorys_set.all()
    return render(request,'Category.html',locals())


def add_category(request):
    # 从数据库取所有关联Uesr的分类
    user_name = request.COOKIES.get("user_name", '')
    # 获取数据库中该用户的对象
    user = User.objects.get(name=user_name)
    fileForm = modelform_factory(categorys, fields=['category', 'cate_img'])
    if request.method=="POST":
        form = fileForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data['category']
            cate_img = form.cleaned_data['cate_img']
            # 写入数据库
            category1= categorys()
            category1.category = category
            category1.cate_img = cate_img
            category1.user_name=User.objects.get(name=user_name)
            category1.save()

        return redirect("/content/category/")
    return render(request,"404.html",locals())


def del_category(request):
    id = request.GET.get('id', 1)
    try:
        category = categorys.objects.get(id=id)
    except:
        return render(request,"test.html",locals())

    categorys.delete(category)
    return redirect("/content/category/")