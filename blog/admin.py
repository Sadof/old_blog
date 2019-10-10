from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_author','post_title','post_text','pub_date')
    list_filter = ('post_author', 'pub_date')
#admin.site.register(Post, PostAdmin)