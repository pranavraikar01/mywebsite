from django.contrib import admin
from .models import Post,Author,Tag 


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    prepopulated_fields={"slug":("title",)}#IT AUTOMATICALLY CALLS SLUGIFY WHICH IS INBUILT
    list_filter = ("author", "tags","date",)     #ADDS FILTER SECTION WHICH INCLUDES THE INPUTS PASSED AS A TUPPLE HERE author and rating
    list_display = ("title","date", "author",)     #displays in a better format WHICH INCLUDES THE INPUTS PASSED AS A TUPPLE HERE author and rating


admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)