from django.contrib import admin

# Register your models here.
from .models import Question1,Choice1

admin.site.register(Question1)
admin.site.register(Choice1)