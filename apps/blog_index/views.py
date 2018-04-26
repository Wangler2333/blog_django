from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.mixin import LoginRequiredMixin
from apps.blog_console.models import BlogHtml
from apps.blog_sign.models import User


# Create your views here.
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
    articles_html = BlogHtml.objects.filter(user=user).order_by('-create_time')
    return render(request, 'index/lw-index-noslider.html', {'articles_html': articles_html, 'user_info': user_info})
