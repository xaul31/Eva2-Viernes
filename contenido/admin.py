from django.contrib import admin
from .models import Perfil, TipoAmenaza, Medio, Pregunta, Opcion, RegistroRespuesta

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'slug', 'activo')
    search_fields = ('nombre',)
    list_filter = ('activo',)

@admin.register(TipoAmenaza)
class TipoAmenazaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Medio)
class MedioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'orden')
    search_fields = ('nombre',)
    list_filter = ('orden',)

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'enunciado', 'perfil', 'tipo_amenaza', 'medio', 'activa')
    search_fields = ('enunciado',)
    list_filter = ('perfil', 'tipo_amenaza', 'medio', 'activa')


@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'pregunta', 'texto', 'es_correcta', 'orden')
    search_fields = ('texto',)
    list_filter = ('es_correcta',)

@admin.register(RegistroRespuesta)
class RegistroRespuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'pregunta', 'opcion', 'fecha_respuesta')
    search_fields = ('usuario__username', 'pregunta__enunciado')
    list_filter = ('fecha_respuesta',)
    readonly_fields = ('fecha_respuesta',)
