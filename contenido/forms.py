from django import forms
from .models import Pregunta, Perfil, TipoAmenaza, Medio, Opcion


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'slug', 'descripcion', 'activo']


class TipoAmenazaForm(forms.ModelForm):
    class Meta:
        model = TipoAmenaza
        fields = ['nombre', 'descripcion']


class MedioForm(forms.ModelForm):
    class Meta:
        model = Medio
        fields = ['nombre', 'orden']


class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['perfil', 'tipo_amenaza', 'medio', 'enunciado', 'mensaje_simulado', 'explicacion', 'puntos', 'activa']


class OpcionForm(forms.ModelForm):
    class Meta:
        model = Opcion
        fields = ['pregunta', 'texto', 'es_correcta', 'retroalimentacion', 'orden']