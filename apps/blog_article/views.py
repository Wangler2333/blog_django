from django.shortcuts import render
from apps.blog_console.models import BlogHtml


# Create your views here.

def index(request):
    return render(request, 'article/lw-article-fullwidth.html')


def article_id(request, article):
    article = article.replace('/', '')
    article = int(article)
    print(article)
    article_html = BlogHtml.objects.get(markdown_id=article)
    try:
        user_info = article_html.user.userinfo
    except:
        user_info = dict()
        user_info['name'] = '没有名字...'
        user_info['introduction'] = '还没有介绍自己...'
    return render(request, 'article/lw-article-fullwidth.html', {'article_html': article_html, 'userinfo': user_info})
