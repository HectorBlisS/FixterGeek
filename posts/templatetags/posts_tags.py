from django import template
register = template.Library()
from ..models import Post

@register.simple_tag(name='otro_nombre')
def total_posts():
	return Post.objects.all().count()

@register.inclusion_tag('posts/los_posts.html')
def show_posts(count=5):
	los_posts = Post.objects.all().order_by('-titulo')[:count]
	return {'posts':los_posts}

@register.assignment_tag
def todos_posts(count=3):
	return Post.objects.all()[:count]
