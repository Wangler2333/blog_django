import os
import time
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.generic import View
from dj_blog import settings
from apps.blog_console.models import BlogMarkdown, BlogHtml
from django.contrib.auth.decorators import login_required
from utils.mixin import LoginRequiredMixin
from django.db.models import Max


# Create your views here.


@login_required
def user(request):
    return render(request, 'console/admin-user.html')


@login_required
def help(request):
    return render(request, 'console/admin-help.html')


@login_required
def gallery(request):
    return render(request, 'console/admin-gallery.html')


@login_required
def table(request):
    return render(request, 'console/admin-table.html')


def save_markdown(article_id, title, markdown_doc, user_login):
    try:
        blog_markdown = BlogMarkdown.objects.get(id=article_id)
    except:
        blog_markdown = BlogMarkdown()
    blog_markdown.id = article_id
    blog_markdown.title = title
    blog_markdown.article = markdown_doc
    blog_markdown.user_id = user_login.id
    blog_markdown.save()
    return JsonResponse({'resultCode': 200})


def save_html(article_id, title, html_code, user_login):
    try:
        blog_html = BlogHtml.objects.get(markdown_id=article_id)
    except:
        blog_html = BlogHtml()
    blog_html.markdown_id = article_id
    blog_html.title = title
    blog_html.article = html_code
    blog_html.user_id = user_login.id
    blog_html.save()
    return JsonResponse({'resultCode': 200})


class FormView(LoginRequiredMixin, View):
    def get(self, request):
        # 新建一个文章编号，暂定使用blog_markdown表的id作为article_id
        max_id = BlogMarkdown.objects.all().aggregate(Max('id'))
        article_id = max_id['id__max'] + 1
        response = render(request, 'console/admin-form.html')
        response.set_cookie('article_id', article_id)
        return response

    def post(self, request: HttpRequest):
        # 获取登录用户对应User对象，查询集类型
        user_login = request.user

        article_id = request.COOKIES.get('article_id')

        # 获取POST提交的数据
        submit = request.POST.get('submit')
        title = request.POST.get('title')
        html_code = request.POST.get('test-editormd-html-code')
        markdown_doc = request.POST.get('test-editormd-markdown-doc')
        # 如果有submit键，则为发布内容
        if submit:
            save_markdown(article_id, title, markdown_doc, user_login)
            save_html(article_id, title, html_code, user_login)
            return HttpResponse('已发布')
        else:
            json_response = save_markdown(article_id, title, markdown_doc, user_login)
            return json_response


@login_required
def upload_image(request):
    # 请求方法为POST时，进行处理
    if request.method == "POST":

        # 获取上传的文件，如果没有文件，则默认为None
        _file = request.FILES.get("editormd-image-file", None)
        if not _file:
            return HttpResponse(json.dumps({'success': 0, 'message': 'upload image failed'}, ensure_ascii=False),
                                content_type="application/json")

        media_root = settings.MEDIA_DIR
        strs = _file.name.split('.')
        suffix = strs[-1]
        file_name = strs[0]
        now_time = str(int(time.time() * 1000))
        file_name = file_name.replace('(', '[').replace(')', ']')
        image_floder = os.path.join(media_root, 'image')
        if not os.path.exists(image_floder):
            os.makedirs(image_floder)

        image_name = file_name + "_" + now_time + "." + suffix
        count = 1
        while os.path.exists(os.path.join(image_floder, image_name)):
            image_name = file_name + "_" + now_time + "[" + str(count) + "]." + suffix
            count += 1

        file_dir = os.path.join(image_floder, image_name)
        destination = open(file_dir, 'wb+')
        for chunk in _file.chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse(json.dumps({'success': 1, 'message': 'upload image successed',
                                        'url': settings.MEDIA_URL + 'image' + "/" + image_name},
                                       ensure_ascii=False), content_type="application/json")
