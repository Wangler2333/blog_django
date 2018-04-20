from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.mixin import LoginRequiredMixin
from apps.blog_console.models import BlogHtml
from apps.blog_sign.models import User


# Create your views here.

def index(request, user_id):
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
        name = user.userinfo.name
    except:
        name = '╮(￣▽￣)╭@'
    articles_html = user.bloghtml_set.all()
    return render(request, 'index/lw-index-noslider.html', {'articles_html': articles_html, 'name':name})
