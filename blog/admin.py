## make it visible on the admin page
from django.contrib import admin 
from .models import Post

admin.site.register (Post)
