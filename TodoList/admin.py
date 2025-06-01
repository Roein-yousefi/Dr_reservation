from django.contrib import admin
from . import models


admin.site.register(models.Todolist)  # Register the Todolist model with the admin site