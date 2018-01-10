from django.contrib import admin

# Register your models here.
from webapi.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'created_time')
    # fields = ('book_name',)


register_list = [(Book, BookAdmin),
                 ]

for item in register_list:
    admin.site.register(item[0], item[1])
