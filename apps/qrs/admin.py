from django.contrib import admin
from .models import URLQR, TextoQR, EmailQR, TarjetaPresentacionQR

@admin.register(URLQR)
class URLQRAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'nombre', 'tamaño', 'redundancia']
    search_fields = ['nombre']
    # Aquí puedes agregar más configuraciones según tus necesidades

@admin.register(TextoQR)
class TextoQRAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'nombre', 'tamaño', 'redundancia']
    search_fields = ['nombre']
    # Aquí puedes agregar más configuraciones según tus necesidades

@admin.register(EmailQR)
class EmailQRAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'nombre', 'tamaño', 'redundancia']
    search_fields = ['nombre']
    # Aquí puedes agregar más configuraciones según tus necesidades

@admin.register(TarjetaPresentacionQR)
class TarjetaPresentacionQRAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'nombre', 'tamaño', 'redundancia']
    search_fields = ['nombre']
    # Aquí puedes agregar más configuraciones según tus necesidades
