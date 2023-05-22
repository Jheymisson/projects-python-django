from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 
    ordering = '-id',
    lister_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name'
    list_per_page = 5
    list_max_show_all = 10
    list_editable = 'first_name', 'last_name', #Isso faz com que aparece campo para editar o objeto
    list_display_links = 'id', 'phone'