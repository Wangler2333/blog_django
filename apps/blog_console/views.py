import os
import time
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from django.views.generic import View
from apps.blog_console.models import BlogMarkdown, BlogHtml
from django.contrib.auth.decorators import login_required
from utils.mixin import LoginRequiredMixin
from django.db.models import Max
from dj_blog import settings
from fdfs_client.client import Fdfs_client


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
    def get(self, request: HttpRequest):
        # 新建一个文章编号，暂定使用blog_markdown表的id作为article_id
        max_id = BlogMarkdown.objects.all().aggregate(Max('id'))

        # {'id__max':int}格式数据
        if max_id['id__max'] is None:
            max_id['id__max'] = 0

        # 新创建一个article_id，并记录进session
        article_id = max_id['id__max'] + 1
        request.session['article_id'] = article_id

        # 返回请求页面
        response = render(request, 'console/admin-form.html')
        return response

    def post(self, request: HttpRequest):
        # 获取登录用户对应User对象，查询集类型
        user_login = request.user

        # 获取article_id，若没有则返回404
        article_id = request.session.get('article_id', None)
        if article_id is None:
            raise Http404("请通过用户中心创建文章")

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
        # 若没有submit键，则为保存内容
        else:
            json_response = save_markdown(article_id, title, markdown_doc, user_login)
            return json_response


@login_required
def upload_image(request):
    # 请求方法为POST时，进行处理
    if request.method == "POST":

        # 获取上传的文件，如果没有文件，则默认为None
        pic = request.FILES.get("editormd-image-file", None)
        # pic = request.FILES['editormd-image-file']
        if not pic:
            return JsonResponse({'success': 0, 'message': 'upload image failed'})

        # 创建一个Fdfs_client对象
        client = Fdfs_client(settings.FDFS_CLIENT_CONF)

        # 上传文件到fast dfs系统中
        res = client.upload_by_buffer(pic.read())
        print(res)

        # dict
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # }
        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件到fast dfs失败')

        # 获取返回的文件ID
        filename = res.get('Remote file_id')

        return JsonResponse({'success': 1, 'message': 'upload image successed',
                             'url': settings.FDFS_URL + filename})
