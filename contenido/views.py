from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Perfil, TipoAmenaza, Medio, Pregunta, Opcion
from .forms import PerfilForm, TipoAmenazaForm, MedioForm, PreguntaForm, OpcionForm
from django.db.models import Count
from django.views import View

class PanelAdminView(TemplateView):
    template_name = 'contenido/panel_admin.html'

# listado de preguntas
class PreguntaListView(ListView):
    model = Pregunta
    template_name = 'contenido/lista/lista_preguntas.html'
    context_object_name = 'preguntas'

    extra_context = {
        'perfiles': Perfil.objects.all(),
        'amenazas': TipoAmenaza.objects.all(),
        'medios': Medio.objects.all()
    }

    def get_queryset(self):
        preguntas = Pregunta.objects.all()
        buscar = self.request.GET.get('buscar')
        perfil = self.request.GET.get('perfil')
        amenaza = self.request.GET.get('amenaza')
        medio = self.request.GET.get('medio')

        if buscar:
            preguntas = preguntas.filter(enunciado__icontains=buscar)

        if perfil:
            preguntas = preguntas.filter(perfil_id=perfil)

        if amenaza:
            preguntas = preguntas.filter(tipo_amenaza_id=amenaza)

        if medio:
            preguntas = preguntas.filter(medio_id=medio)

        return preguntas

# crear pregunta
class PreguntaCreateView(CreateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'contenido/formulario/formulario_pregunta.html'
    success_url = reverse_lazy('lista_preguntas')

# editar pregunta
class PreguntaUpdateView(UpdateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'contenido/formulario/formulario_pregunta.html'
    success_url = reverse_lazy('lista_preguntas')

# eliminar pregunta
class PreguntaDeleteView(DeleteView):
    model = Pregunta
    template_name = 'contenido/eliminar/eliminar_pregunta.html'
    success_url = reverse_lazy('lista_preguntas')

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, 'No puedes eliminar una pregunta con opciones asociadas.')
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())


# Crud de perfiles
class PerfilListView(ListView):
    model = Perfil
    template_name = 'contenido/lista/lista_perfiles.html'
    context_object_name = 'perfiles'

class PerfilCreateView(CreateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'contenido/formulario/formulario_perfil.html'
    success_url = reverse_lazy('lista_perfiles')

class PerfilUpdateView(UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'contenido/formulario/formulario_perfil.html'
    success_url = reverse_lazy('lista_perfiles')

class PerfilDeleteView(DeleteView):
    model = Perfil
    template_name = 'contenido/eliminar/eliminar_perfil.html'
    success_url = reverse_lazy('lista_perfiles')

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, 'No puedes eliminar un perfil con preguntas asociadas.')
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())


# Crud de tipos de amenaza
class TipoAmenazaListView(ListView):
    model = TipoAmenaza
    template_name = 'contenido/lista/lista_amenazas.html'
    context_object_name = 'amenazas'

class TipoAmenazaCreateView(CreateView):
    model = TipoAmenaza
    form_class = TipoAmenazaForm
    template_name = 'contenido/formulario/formulario_amenaza.html'
    success_url = reverse_lazy('lista_amenazas')

class TipoAmenazaUpdateView(UpdateView):
    model = TipoAmenaza
    form_class = TipoAmenazaForm
    template_name = 'contenido/formulario/formulario_amenaza.html'
    success_url = reverse_lazy('lista_amenazas')

class TipoAmenazaDeleteView(DeleteView):
    model = TipoAmenaza
    template_name = 'contenido/eliminar/eliminar_amenaza.html'
    success_url = reverse_lazy('lista_amenazas')

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, 'No puedes eliminar un tipo de amenaza con preguntas asociadas.')
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())


# Crud de medios
class MedioListView(ListView):
    model = Medio
    template_name = 'contenido/lista/lista_medios.html'
    context_object_name = 'medios'

class MedioCreateView(CreateView):
    model = Medio
    form_class = MedioForm
    template_name = 'contenido/formulario/formulario_medio.html'
    success_url = reverse_lazy('lista_medios')


class MedioUpdateView(UpdateView):
    model = Medio
    form_class = MedioForm
    template_name = 'contenido/formulario/formulario_medio.html'
    success_url = reverse_lazy('lista_medios')

class MedioDeleteView(DeleteView):
    model = Medio
    template_name = 'contenido/eliminar/eliminar_medio.html'
    success_url = reverse_lazy('lista_medios')

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, 'No puedes eliminar un medio con preguntas asociadas.')
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())


# Crud de opciones
class OpcionListView(ListView):
    model = Opcion
    template_name = 'contenido/lista/lista_opciones.html'
    context_object_name = 'opciones'


class OpcionCreateView(CreateView):
    model = Opcion
    form_class = OpcionForm
    template_name = 'contenido/formulario/formulario_opcion.html'
    success_url = reverse_lazy('lista_opciones')

class OpcionUpdateView(UpdateView):
    model = Opcion
    form_class = OpcionForm
    template_name = 'contenido/formulario/formulario_opcion.html'
    success_url = reverse_lazy('lista_opciones')

class OpcionDeleteView(DeleteView):
    model = Opcion
    template_name = 'contenido/eliminar/eliminar_opcion.html'
    success_url = reverse_lazy('lista_opciones')

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, 'No puedes eliminar una opción con preguntas asociadas.')
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())


# Cuestionario view

class CuestionarioListView(ListView):
    model = Pregunta
    template_name = 'contenido/cuestionario.html'
    context_object_name = 'preguntas'

    def get_queryset(self):
        preguntas = Pregunta.objects.filter(activa=True)

        preguntas = preguntas.annotate(total_opciones=Count('opciones')).filter(total_opciones=3)

        preguntas = [
            pregunta for pregunta in preguntas if pregunta.opciones.filter(es_correcta=True).count() == 1
        ]

        return preguntas



# responder cuestionario

class ResponderPreguntaView(View):
    def post(self, request, pk):
        pregunta = get_object_or_404(Pregunta, pk=pk, activa=True)

        opcion = get_object_or_404(
            Opcion,
            pk=request.POST.get('opcion'),
            pregunta=pregunta
        )

        if opcion.es_correcta:
            messages.success(
                request,
                '¡Respuesta correcta! ' + opcion.retroalimentacion
            )
        else:
            messages.error(
                request,
                'Respuesta incorrecta. ' + opcion.retroalimentacion
            )

        return redirect('cuestionario')