from django.shortcuts import render
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Perfil, TipoAmenaza, Medio, Pregunta, Opcion
from .forms import PerfilForm, TipoAmenazaForm, MedioForm, PreguntaForm, OpcionForm

class PanelAdminView(TemplateView):
    template_name = 'contenido/panel_admin.html'

# listado de preguntas
class PreguntaListView(ListView):
    model = Pregunta
    template_name = 'contenido/lista_preguntas.html'
    context_object_name = 'preguntas'

# crear pregunta
class PreguntaCreateView(CreateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'contenido/formulario_pregunta.html'
    success_url = reverse_lazy('lista_preguntas')

# editar pregunta
class PreguntaUpdateView(UpdateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'contenido/formulario_pregunta.html'
    success_url = reverse_lazy('lista_preguntas')

# eliminar pregunta
class PreguntaDeleteView(DeleteView):
    model = Pregunta
    template_name = 'contenido/eliminar_pregunta.html'
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
    template_name = 'contenido/lista_perfiles.html'
    context_object_name = 'perfiles'

class PerfilCreateView(CreateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'contenido/formulario_perfil.html'
    success_url = reverse_lazy('lista_perfiles')

class PerfilUpdateView(UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'contenido/formulario_perfil.html'
    success_url = reverse_lazy('lista_perfiles')

class PerfilDeleteView(DeleteView):
    model = Perfil
    template_name = 'contenido/eliminar_perfil.html'
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
    template_name = 'contenido/lista_amenazas.html'
    context_object_name = 'amenazas'

class TipoAmenazaCreateView(CreateView):
    model = TipoAmenaza
    form_class = TipoAmenazaForm
    template_name = 'contenido/formulario_amenaza.html'
    success_url = reverse_lazy('lista_amenazas')

class TipoAmenazaUpdateView(UpdateView):
    model = TipoAmenaza
    form_class = TipoAmenazaForm
    template_name = 'contenido/formulario_amenaza.html'
    success_url = reverse_lazy('lista_amenazas')

class TipoAmenazaDeleteView(DeleteView):
    model = TipoAmenaza
    template_name = 'contenido/eliminar_amenaza.html'
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
    template_name = 'contenido/lista_medios.html'
    context_object_name = 'medios'

class MedioCreateView(CreateView):
    model = Medio
    form_class = MedioForm
    template_name = 'contenido/formulario_medio.html'
    success_url = reverse_lazy('lista_medios')


class MedioUpdateView(UpdateView):
    model = Medio
    form_class = MedioForm
    template_name = 'contenido/formulario_medio.html'
    success_url = reverse_lazy('lista_medios')

class MedioDeleteView(DeleteView):
    model = Medio
    template_name = 'contenido/eliminar_medio.html'
    success_url = reverse_lazy('lista_medios')

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, 'No puedes eliminar un medio con preguntas asociadas.')
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())