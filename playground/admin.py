from django.contrib import admin
from .models import *

admin.site.register(Score)


@admin.register(ChatMessage)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("sender", "message", "send_at")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name",)


# Register your models here.

@admin.register(Word)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("sender", "message", "count")
