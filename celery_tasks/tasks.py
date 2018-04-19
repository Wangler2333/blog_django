from celery import Celery
from dj_blog import settings
from django.core.mail import send_mail

app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/8')

# 在任务处理者一端加这几句
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_blog.settings")
django.setup()


@app.task
def send_register_active_email(to_email, username, token):
    '''发送激活邮件'''
    # 组织邮件信息
    subject = 'LeeBlog欢迎信息'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '<h1>%s, 欢迎您成为LeeBlog注册会员</h1>请点击下面链接激活您的账户<br/><a href="http://127.0.0.1:8000/sign/active/%s">http://127.0.0.1:8000/sign/active/%s</a>' % (
        username, token, token)

    send_mail(subject, message, sender, receiver, html_message=html_message)
