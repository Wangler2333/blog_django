from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.decorators import login_required
from utils.mixin import LoginRequiredMixin
from apps.blog_console.models import BlogHtml, BlogImage
from apps.blog_sign.models import User, UserInfo


# Create your views here.
def img(request, user_id):
    user_info = UserInfo.objects.get(user_id=user_id)
    images = BlogImage.objects.filter(user_id=user_id)
    return render(request, 'index/lw-img.html', {"images": images, "user_info": user_info, "user_id": user_id})


def index(request):
    user_login = request.user
    if user_login.is_authenticated():
        return redirect('/index/%s' % user_login.id)
    return redirect('sign:login')


def user_index(request, user_id):
    user_login = request.user
    if user_login.is_authenticated():
        if not user_id:
            return redirect('/index/%s' % user_login.id)
        if user_login.id == user_id:
            pass
    if not user_id:
        return redirect('sign:login')
    user = User.objects.get(id=user_id)
    try:
        user_info = user.userinfo
    except:
        user_info = dict()
        user_info['name'] = '没有名字...'
        user_info['introduction'] = '还没有介绍自己...'
    articles_html = BlogHtml.objects.filter(user=user, is_delete=False, is_show=True).order_by('-update_time')
    return render(request, 'index/lw-index-noslider.html',
                  {'articles_html': articles_html, 'user_info': user_info, 'user_id': user_id})
