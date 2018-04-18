from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login


# 背景图片数量


# Create your views here.

class LoginView(View):
    def get(self, request: HttpRequest):
        # get请求返回登录页面
        return render(request, 'sign/lw-log.html')

    def post(self, request: HttpRequest):
        # post请求则进行校验
        username_email = request.POST['email']
        password = request.POST['password']
        # 校验username_email和password是否为空
        if not all([username_email, password]):
            return render(request, 'sign/lw-error.html', {'error': '信息不完整'})
        # 则校验用户名和密码与数据库对比
        db_user = authenticate(username=username_email, password=password)
        # 校验错误返回None，正确返回查询对象
        if not db_user:
            return render(request, 'sign/lw-error.html', {'error': '账号密码错误'})
        # 判断邮箱是否激活
        if not db_user.is_active:
            return render(request, 'sign/lw-error.html', {'error': '邮箱未激活'})
        # 校验全部通过则回到主页
        return redirect('index:index')


class Register(View):
    def get(self, request: HttpRequest):
        return render(request, 'sign/lw-re.html')


class ForgetView(View):
    def get(self, request: HttpRequest):
        return render(request, 'sign/lw-forget.html')
