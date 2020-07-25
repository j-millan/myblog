from django.contrib import admin
from .models import BlogPost, BlogComment, UserFollowing, BlogCategory

admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(UserFollowing)
admin.site.register(BlogCategory)