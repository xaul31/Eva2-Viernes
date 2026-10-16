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

    def clean(self):
        datos = super().clean()

        pregunta = datos.get('pregunta')
        es_correcta = datos.get('es_correcta')

        if pregunta:
            opciones = Opcion.objects.filter(pregunta=pregunta)

            # Excluir la opción actual cuando se está editando
            if self.instance.pk:
                opciones = opciones.exclude(pk=self.instance.pk)

            # Validar máximo de tres alternativas
            if opciones.count() >= 3:
                raise forms.ValidationError(
                    'Esta pregunta ya tiene tres alternativas.'
                )

            # Validar una sola respuesta correcta
            if es_correcta and opciones.filter(es_correcta=True).exists():
                raise forms.ValidationError(
                    'Esta pregunta ya tiene una respuesta correcta.'
                )

        return datos


class RespuestaForm(forms.Form):
    opcion = forms.ModelChoiceField(
        queryset=Opcion.objects.all(),
        widget=forms.RadioSelect,
        label='Seleccione una alternativa'
    )
