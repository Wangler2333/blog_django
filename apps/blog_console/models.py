from django.db import models
from db_model.base_model import BaseModel
from apps.blog_sign.models import User
from django.db.models.signals import post_delete
import os


# Create your models here.

class BlogMarkdown(BaseModel):
    user = models.ForeignKey(User, verbose_name='作者')
    title = models.CharField(max_length=30, verbose_name='标题')
    article = models.TextField(verbose_name='文章')

    def __str__(self):
        s = '【' + str(self.user_id) + '】' + self.title
        return s

    class Meta:
        db_table = 'blog_markdown'
        verbose_name = 'Markdown列表'
        verbose_name_plural = verbose_name


class BlogHtml(BaseModel):
    user = models.ForeignKey(User, verbose_name='作者')
    title = models.CharField(max_length=30, verbose_name='标题')
    article = models.TextField(verbose_name='文章')
    markdown = models.OneToOneField(BlogMarkdown, verbose_name='markdown文章ID')

    def __str__(self):
        s = '【' + str(self.user_id) + '】' + self.title
        return s

    class Meta:
        db_table = 'blog_html'
        verbose_name = 'Html列表'
        verbose_name_plural = verbose_name


class BlogImage(BaseModel):
    user = models.ForeignKey(User, verbose_name='作者')
    article = models.ForeignKey(BlogMarkdown, null=True, blank=True, verbose_name='所属文章')
    title = models.CharField(max_length=30, verbose_name='描述')
    image = models.ImageField(upload_to='image', verbose_name='图片')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_image'
        verbose_name = '图片列表'
        verbose_name_plural = verbose_name


# 用于在删除数据表里的记录时，同步删除文件
# 使用信号触发
def delete_image_file(sender, **kwargs):
    patch = kwargs['instance']
    os.remove(patch.image.path)


def delete_markdown_file(sender, **kwargs):
    patch = kwargs['instance']
    os.remove(patch.article.path)


post_delete.connect(delete_image_file, sender=BlogImage)
post_delete.connect(delete_markdown_file, sender=BlogMarkdown)
