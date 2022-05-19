from django.contrib import admin
from .models import Author, Book
# Register your models here.
#create Admin class:
class BookAdmin(admin.ModelAdmin):
   #readonly_fields=("slug",) to avoid error
   prepopulated_fields={"slug": ("title",)} 
   list_filter= ("author","rating")
   list_display=("title", "author")

# class AuthorAdmin(admin.ModelAdmin):
#    list_display=("first_name", "last_name")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)