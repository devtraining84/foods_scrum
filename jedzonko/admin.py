from django.contrib import admin
from .models import Receipe, Plan, Dayname, Recipeplan

admin.site.register(Receipe)
admin.site.register(Plan)
admin.site.register(Dayname)
admin.site.register(Recipeplan)
