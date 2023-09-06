from django.contrib import admin

from AppCoder import models
# Register your models here.

admin.site.register(models.curso)
admin.site.register(models.estudiantes)
admin.site.register(models.profesores)

