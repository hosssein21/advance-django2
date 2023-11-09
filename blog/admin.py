from django.contrib import admin
from .models import Post,Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ["title","Active","updated_time"]
    list_filter=('Active',)
    search_fields=["title","content"]
    date_hierarchy="created_time"
    
    
admin.site.register(Category)