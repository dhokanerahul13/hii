from django.contrib import admin

# Register your models here.
from stu.models import movie

class movieadmin(admin.ModelAdmin):
    list_display=['rdate','moviename','rating']
admin.site.register(movie,movieadmin)    