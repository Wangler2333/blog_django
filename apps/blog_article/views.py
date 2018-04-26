from django.shortcuts import render
from django.http import Http404
from apps.blog_console.models import BlogHtml


# Create your views here.

def index(request):
    return render(request, 'article/lw-article-fullwidth.html')


def article_id(request, article):
    # 若请求的路径含有/则去除
    article = article.replace('/', '')
    article = int(article)

    # 获取相应的html格式文章
    try:
        article_html = BlogHtml.objects.get(markdown_id=article)
    except:
        raise Http404("文章不存在")
    # user_articles = article_html.user.bloghtml_set.order_by('markdown_id')
    # try:
    #     article_prev = user_articles.filter(markdown_id__lt=article).order_by('-markdown_id')[0]
    # except:
    #     article_prev = None
    # try:
    #     article_next = user_articles.filter(markdown_id__gt=article)[0]
    # except:
    #     article_next = None
    try:
        user_info = article_html.user.userinfo
    except:
        user_info = dict()
        user_info['name'] = '没有名字...'
        # user_info['qq_id'] = '还没有填写'
        # user_info['wechat_id'] = '还没有填写'
        # user_info['weibo_id'] = '还没有填写'
        # user_info['github_id'] = '还没有填写'
        user_info['introduction'] = '还没有介绍自己...'
    return render(request, 'article/lw-article-fullwidth.html', {'article_html': article_html, 'userinfo': user_info})
