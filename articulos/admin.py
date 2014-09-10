from django.contrib import admin
from articulos.models import  Articulo, Comentario

class ArticuloAdmin(admin.ModelAdmin):
    list_display=['titulo','contenido','fecha_pub','categoria']
    list_filter=['autor']

class ComentarioAdmin(admin.ModelAdmin):
    list_display=['texto','fecha']
    list_filter=['articulo']

admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentario, ComentarioAdmin)
