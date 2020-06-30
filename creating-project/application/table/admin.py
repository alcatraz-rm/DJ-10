from django.contrib import admin

# Register your models here.
from table.models import Column, FilePath


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass


@admin.register(FilePath)
class FilePathAdmin(admin.ModelAdmin):
    pass
