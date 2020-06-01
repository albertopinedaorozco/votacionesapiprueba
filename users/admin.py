from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile


#admin.site.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id','username','first_name','last_name', 'is_staff', 'es_lider')
    list_filter = ('es_lider','is_staff','creado','modificado')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','votantes_registrados')
    search_fields = ('user__username','user__first_name','user__last_name')
    list_filter = ('votantes_registrados',)

admin.site.register(User, CustomUserAdmin)


