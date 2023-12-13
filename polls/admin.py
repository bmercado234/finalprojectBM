
from django.contrib import admin

from .models import Choice, Question

# Choice model displayed in the question admin page
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Configuration for question model in admin interface
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]



# Register your models here.
admin.site.register(Question, QuestionAdmin)
