from django import forms

class Userform(forms.Form):
    username = forms.CharField(label="UserName", max_length=128, widget=forms.TextInput(attrs={}))
    password = forms.CharField(label="PassWord", max_length=256, widget=forms.PasswordInput(attrs={ }))


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={}))
    password1 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={}))
    number = forms.CharField(label='手机号',max_length=11, widget=forms.TextInput(attrs={}))