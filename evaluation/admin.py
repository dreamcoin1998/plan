from django.contrib import admin
from .models import Evaluation

# Register your models here.
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('id', 'star', 'score', 'evaluation_text', 'comment_time', 'content_object')
    ordering = ('id',)


admin.site.register(Evaluation)