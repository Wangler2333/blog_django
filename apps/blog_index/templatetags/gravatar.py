# gravatar.com头像获取过滤器
# 使用官方libgravatar模块

from django import template
import libgravatar

register = template.Library()


@register.filter
def gravatar_get_image(email):
    g = libgravatar.Gravatar(email=email)
    # get_image(size=80, default='', force_default=False, rating='', filetype_extension=False, use_ssl=False)
    # http://en.gravatar.com/site/implement/images/
    image_url = g.get_image(default='retro')
    return image_url
