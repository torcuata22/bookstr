from django.contrib import admin
from .models import Book
# Register your models here.
#create Admin class:
class BookAdmin(admin.ModelAdmin):
   #readonly_fields=("slug",) to avoid error
   prepopulated_fields={"slug": ("title",)} 
   list_filter= ("author","rating")
   list_display=("title", "author")


admin.site.register(Book, BookAdmin)