from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login
from apps.blog_sign.models import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from dj_blog import settings
from celery_tasks.tasks import send_register_active_email
import re


# 背景图片数量


# Create your views here.

class LoginView(View):
    """
    Login登录的类视图，可区分请求类型
    """

    def get(self, request: HttpRequest):  # request: HttpRequest用于标识类型
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
        # 校验全部通过则回到主页，逆向解析url
        return redirect(reverse('index:index'))


class Register(View):
    """
    Register注册的类视图，可区分请求类型
    """

    def get(self, request: HttpRequest):
        # get请求返回注册页面
        return render(request, 'sign/lw-re.html')

    def post(self, request: HttpRequest):
        # post请求则进行校验
        username_email = request.POST['email']
        password = request.POST['password']
        # 校验username_email和password是否为空
        if not all([username_email, password]):
            return render(request, 'sign/lw-error.html', {'error': '信息不完整'})
        # 校验邮箱格式
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', username_email):
            return render(request, 'sign/lw-error.html', {'error': '邮箱格式不正确'})
        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username_email)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名已存在
            return render(request, 'sign/lw-error.html', {'errmsg': '用户名已存在'})

        # 进行业务处理: 进行用户注册
        user = User.objects.create_user(username_email, username_email, password)
        user.is_active = 0
        user.save()

        # 发送激活邮件，包含激活链接: http://127.0.0.1:8000/user/active/3
        # 激活链接中需要包含用户的身份信息, 并且要把身份信息进行加密

        # 加密用户的身份信息，生成激活token
        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': user.id}
        token = serializer.dumps(info)  # bytes
        token = token.decode()

        # 发邮件(email,username,token)
        send_register_active_email.delay(username_email, username_email, token)

        # 返回应答, 跳转到首页
        return redirect(reverse('index:index'))


class ForgetView(View):
    """
    Forget忘记密码的类视图，可区分请求类型
    """

    def get(self, request: HttpRequest):
        return render(request, 'sign/lw-forget.html')
