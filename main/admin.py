"""from django.contrib import admin
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    fields = ["tutorial_title",
              "tutorial_published",
              "tutorial_content"]

admin.site.register(Tutorial,TutorialAdmin)"""
from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib import admin
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Tutorial,TutorialAdmin)