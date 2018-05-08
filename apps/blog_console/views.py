import os
import time
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from django.views.generic import View
from apps.blog_console.models import BlogMarkdown, BlogHtml, BlogImage, BlogArticleId, BlogImageThumbs
from apps.blog_sign.models import UserInfo
from django.contrib.auth.decorators import login_required
from utils.mixin import LoginRequiredMixin
from django.db.models import Max
from dj_blog import settings
from fdfs_client.client import Fdfs_client
from PIL import ImageFile, Image, ImageDraw
from django.utils.six import BytesIO
import copy
import re


# Create your views here.


class UserView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        login_user = request.user
        # 查找登录人员的信息，并输出给模板显示
        try:
            user_info = login_user.userinfo
        except:
            user_info = None
        return render(request, 'console/admin-user.html', {'user_info': user_info})

    def post(self, request: HttpRequest):
        # 提取post传来的数据
        post = request.POST
        name = post.get('user-name', default='')
        qq = post.get('user-qq', default='')
        weibo = post.get('user-weibo', default='')
        github = post.get('user-github', default='')
        wechat = post.get('user-wechat', default='')
        introduction = post.get('user-intro', default='')

        # 如果有此人数据则更新，否则新建
        try:
            user_info = UserInfo.objects.get(user=request.user)
        except:
            user_info = UserInfo()
        user_info.user = request.user
        user_info.name = str(name)
        user_info.qq_id = str(qq)
        user_info.weibo_id = str(weibo)
        user_info.github_id = str(github)
        user_info.wechat_id = str(wechat)
        user_info.introduction = str(introduction)
        user_info.save()
        return JsonResponse({'resultCode': 200})


class GalleryView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        login_user = request.user
        user_images = BlogImage.objects.filter(user=login_user, is_delete=False).order_by('-update_time')
        return render(request, 'console/admin-gallery.html', {'images': user_images})

    def post(self, request: HttpRequest):
        post = request.POST
        post_name = post.get(key='name', default=None)
        post_value = post.get(key='value', default=None)
        post_title = post.get(key='title', default=None)
        post_show = post.get(key='show', default=None)
        post_image_id = post.get(key='image_id', default=None)

        # 如果是多选删除按钮
        if post_name == 'delete_select':

            # 切割str数据为列表，最后一个为空，舍弃
            values = post_value.split(',')[:-1]

            # 新建一个列表保存删除的markdown的id
            li_list = list()
            for value in values:
                # 逐条获取markdown对象并删除
                image = BlogImage.objects.get(id=value)
                # 由于模型类设置了on_delete=models.CASCADE，则其外键BlogHtml相关数据一起删除
                image.delete()
                li_list.append(value)

            # 将li_list列表传回ajax作为数组，供其删除相应元素
            return JsonResponse({'resultCode': 200, 'li_list': li_list})

        # 如果是单个删除按钮
        if post_name == 'delete':
            # 过程同上
            value = post_value
            image = BlogImage.objects.get(id=value)
            image.delete()
            return JsonResponse({'resultCode': 201, 'li_list': value})

        if post_name == 'set_select':

            # 切割str数据为列表，最后一个为空，舍弃
            values = post_value.split(',')[:-1]

            # 新建一个列表保存删除的markdown的id
            true_list = list()
            false_list = list()
            for value in values:
                # 逐条获取markdown对象并删除
                image = BlogImage.objects.get(id=value)
                if image.is_show:
                    image.is_show = False
                    false_list.append(value)
                else:
                    image.is_show = True
                    true_list.append(value)
                image.save()

            # 将li_list列表传回ajax作为数组，供其删除相应元素
            return JsonResponse({'resultCode': 202, 'true_list': true_list, 'false_list': false_list})

        # 如果是弹出框发来的请求
        if post_image_id:
            image = BlogImage.objects.get(id=post_image_id)
            if post_title:
                image.title = post_title
            if post_show:
                image.is_show = True
            else:
                image.is_show = False
            image.save()
            return JsonResponse({'resultCode': 200, 'id': post_image_id, 'title': post_title, 'show': post_show})
        print(post)


class TableView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        login_user = request.user

        # 区分是访问页面还是修改文章
        get = request.GET
        try:
            # 使用字典提取的方法，没有键会触发异常，所以采用try
            # 保存此篇文章的article_id，用于发布和保存
            article_id = get['edit']
            request.session['article_id'] = article_id
            markdown = BlogMarkdown.objects.get(id=article_id)
            return render(request, 'console/admin-form.html', {'markdown': markdown, 'article_id': article_id})
        except:
            pass

        # 访问网站则返回table页面
        user_markdown = BlogMarkdown.objects.filter(user=login_user, is_delete=False).order_by('-update_time')
        return render(request, 'console/admin-table.html', {'markdowns': user_markdown})

    def post(self, request: HttpRequest):
        # 获取post传来的数据
        post = request.POST
        post_name = post.get(key='name', default=None)
        post_value = post.get(key='value', default=None)

        # 如果是多选删除按钮
        if post_name == 'delete_select':

            # 切割str数据为列表，最后一个为空，舍弃
            values = post_value.split(',')[:-1]

            # 新建一个列表保存删除的markdown的id
            li_list = list()
            for value in values:
                # 逐条获取markdown对象并删除
                markdown = BlogMarkdown.objects.get(id=value)
                # 由于模型类设置了on_delete=models.CASCADE，则其外键BlogHtml相关数据一起删除
                markdown.delete()
                li_list.append(value)

            # 将li_list列表传回ajax作为数组，供其删除相应元素
            return JsonResponse({'resultCode': 200, 'li_list': li_list})

        # 如果是单个删除按钮
        if post_name == 'delete':
            # 过程同上
            value = post_value
            markdown = BlogMarkdown.objects.get(id=value)
            markdown.delete()
            return JsonResponse({'resultCode': 201, 'li_list': value})


def save_markdown(article_id, title, markdown_doc, user_login):
    """
    保存数据到markdown数据库
    :param article_id: 作为id
    :param title: 作为title
    :param markdown_doc: 作为article
    :param user_login: 作为user外键数据
    :return: json数据{'resultCode': 200}
    """
    try:
        blog_markdown = BlogMarkdown.objects.get(id=article_id)
    except:
        blog_markdown = BlogMarkdown()
    blog_markdown.id = article_id
    blog_markdown.title = title
    blog_markdown.article = markdown_doc
    blog_markdown.user = user_login
    blog_markdown.save()
    try:
        # 查找BlogHtml中相关文章，标记为未发布
        blog_html = BlogHtml.objects.get(markdown_id=article_id)
        blog_html.is_show = False
        blog_html.save()
    except:
        pass
    return JsonResponse({'resultCode': 200})


def save_html(article_id, title, html_code, user_login):
    """
    保存数据到html数据库
    :param article_id: 作为markdown外键数据
    :param title: 作为title
    :param html_code: 作为article
    :param user_login: 作为user外键数据
    :return: json数据{'resultCode': 200}
    """
    try:
        # 如果存在则更新，否则新建
        blog_html = BlogHtml.objects.get(markdown_id=article_id)
    except:
        blog_html = BlogHtml()
    blog_html.markdown_id = article_id
    blog_html.title = title
    blog_html.article = html_code
    blog_html.user = user_login
    # 将发布标记设为True
    blog_html.is_show = True
    blog_html.save()
    return JsonResponse({'resultCode': 200})


def article_image(article_id, html_code, user_login):
    """
    用于标记图片所属文章
    :param article_id:
    :param html_code:
    :param user_login:
    :return:
    """
    images = re.findall(r'\"%s(.+?)\"' % settings.FDFS_URL, html_code)
    for image_name in images:
        blog_images = BlogImage.objects.filter(image=image_name, user=user_login)
        for blog_image in blog_images:
            blog_image.article_id = article_id
            blog_image.save()


class FormView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        # 新建一个article_id用于标识文章的唯一性
        blog_article_id = BlogArticleId()
        blog_article_id.user = request.user
        blog_article_id.save()
        article_id = blog_article_id.id

        # 新创建一个article_id，并记录进session
        request.session['article_id'] = article_id

        # 返回请求页面
        response = render(request, 'console/admin-form.html', {'article_id': article_id})
        return response

    def post(self, request: HttpRequest):
        # 获取登录用户对应User对象，查询集类型
        user_login = request.user

        # 获取article_id，若没有则返回404
        article_id = request.session.get('article_id', None)
        if article_id is None:
            raise Http404("请通过用户中心创建文章")

        # 获取POST提交的数据
        button_name = request.POST.get('button_name')
        title = request.POST.get('title')
        html_code = request.POST.get('test-editormd-html-code')
        markdown_doc = request.POST.get('test-editormd-markdown-doc')

        if not title:
            return JsonResponse({'resultCode': 501})

        if not html_code:
            return JsonResponse({'resultCode': 502})

        # 如果有submit键，则为发布内容
        if button_name == 'submit':
            save_markdown(article_id, title, markdown_doc, user_login)
            save_html(article_id, title, html_code, user_login)
            article_image(article_id, html_code, user_login)
            return JsonResponse({'resultCode': 304})
        # 若没有submit键，则为保存内容
        if button_name == 'save':
            json_response = save_markdown(article_id, title, markdown_doc, user_login)
            return json_response
        else:
            return Http404("没有这个功能")


def thumbnail_img(img):
    """
    对图片进行压缩处理，得到缩略图
    :param img: Django的File文件
    :return: BytesIO的内存数据，file-like object
    """
    # 创建BytesIO对象
    image_file = BytesIO()

    # 读取img数据，生成Pillow图片对象
    p = ImageFile.Parser()
    p.feed(img.read())
    image = p.close()

    # 获取原图宽高
    width = image.width
    height = image.height

    # 设置最大宽高
    max_len = 300

    # 图片缩放
    if width <= max_len and height <= max_len:
        pass
    else:
        if width >= height:
            height_image = max_len * height // width
            image.thumbnail((max_len, height_image), Image.ANTIALIAS)
        if width < height:
            width_image = max_len * width // height
            image.thumbnail((width_image, max_len), Image.ANTIALIAS)

    # 图片保存
    image.save(image_file, 'png')  # 保存到内存

    return image_file, image.size


@login_required
def upload_image(request):
    # 请求方法为POST时，进行处理
    if request.method == "POST":

        # 获取上传的文件，如果没有文件，则默认为None
        pic = request.FILES.get("editormd-image-file", None)

        # # 对pic的保存，消耗了其数据，所以需要做一份拷贝
        # img = copy.deepcopy(pic)

        # pic = request.FILES['editormd-image-file']
        if not pic:
            return JsonResponse({'success': 0, 'message': 'upload image failed'})

        #####################################保存原图
        # 创建图片模型类对象
        # image字段保存图片使用指定的storage方法，上传到FastDFS
        image = BlogImage()
        image.user = request.user
        image.title = pic.name
        image.image = pic
        image.save()
        # #####################################保存缩略图
        # # 调用Pillow模块生成缩略图，得到BytesIO()对象
        # image_file, size = thumbnail_img(img)
        # # 读取BytesIO数据
        # image_thumbnail = image_file.getvalue()
        # image_file.close()
        #
        # # 创建一个Fdfs_client对象
        # client = Fdfs_client(settings.FDFS_CLIENT_CONF)
        #
        # # 上传数据到fast dfs系统中
        # res = client.upload_by_buffer(image_thumbnail)
        # if res.get('Status') != 'Upload successed.':
        #     # 上传失败
        #     raise Exception('上传文件到fast dfs失败')
        # # 获取返回的文件ID
        # filename = res.get('Remote file_id')
        #
        # image_thumb = BlogImageThumbs()
        # image_thumb.image = image
        # image_thumb.image_thumb = filename
        # image_thumb.width = size[0]
        # image_thumb.height = size[1]
        # image_thumb.save()
        # #####################################
        return JsonResponse({'success': 1, 'message': 'upload image successed',
                             'url': image.image.url})
