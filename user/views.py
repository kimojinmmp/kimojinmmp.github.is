from django.shortcuts import render, redirect
from . import forms
# Create your views here.
from .models import User


def login_or_signup(request):
    print(request.COOKIES.get("is_login"))
    if request.COOKIES.get("is_login","") is True:
        return redirect("/content/index/")
    if request.method=='POST':
        message='请填写账号信息'
        if request.POST.get('password1'):
            user_data = forms.RegisterForm(request.POST)
            if user_data.is_valid():
                username = user_data.cleaned_data.get('username')
                password = user_data.cleaned_data.get('password')
                email = user_data.cleaned_data.get('email')
                number = user_data.cleaned_data.get('number')

                if User.objects.filter(name=username):
                    message = '该用户名已注册'
                    return render(request, 'LoginAndSignUp.html',locals())
                if User.objects.filter(number=number):
                    message = '该手机号已注册'
                    return render(request, 'LoginAndSignUp.html', locals())
                if password!=user_data.cleaned_data.get('password1'):
                    message = '两次输入的密码不相同'
                    return render(request, 'LoginAndSignUp.html', locals())
                message='注册成功！'
                user=User()
                user.name=username
                user.email=email
                user.number=number
                user.password=password
                user.save()
                return render(request, 'LoginAndSignUp.html', locals())
            return render(request, 'LoginAndSignUp.html', locals())
        else:
            # if request.session.get('is_login'):
            #     return redirect('/content/index/')
            user_data = forms.Userform(request.POST)
            if user_data.is_valid():
                username = user_data.cleaned_data.get('username')
                password = user_data.cleaned_data.get('password')
                try:
                    user=User.objects.get(name=username)
                except:
                    message = '用户不存在'
                    return render(request, 'LoginAndSignUp.html', locals())
                if user.password == password:
                    message='登录成功!'
                    req=redirect('/content/index/')
                    req.set_cookie("is_login",value=True)
                    req.set_cookie("user_name", value=user.name)
                    req.set_cookie("user_pwd", value=user.password)
                    return req
                else:
                    message='密码错误！'
                    return render(request, 'LoginAndSignUp.html', locals())
            return render(request, 'LoginAndSignUp.html', locals())
    else:
        user_data = forms.RegisterForm()
        return render(request, 'LoginAndSignUp.html', locals())
