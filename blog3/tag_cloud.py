from django import template
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag("blog3/tag_cloud.html")
def sidebar_tag_cloud():
    x = Tag.objects.all()
    return {"tags": x}
