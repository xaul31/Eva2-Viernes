from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Perfil, TipoAmenaza, Medio, Pregunta, Opcion, RegistroRespuesta
from .forms import PerfilForm, TipoAmenazaForm, MedioForm, PreguntaForm, OpcionForm, RegistroForm
from django.db.models import Count
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.http import url_has_allowed_host_and_scheme


class AdminRequeridoMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'No tienes permiso para acceder a esta página.')
            return redirect('cuestionario')
        return super().handle_no_permission()

class PanelAdminView(AdminRequeridoMixin, TemplateView):
    template_name = 'contenido/panel_admin.html'

# listado de preguntas
class PreguntaListView(AdminRequeridoMixin, ListView):
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
class PreguntaCreateView(AdminRequeridoMixin, CreateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'contenido/formulario/formulario_pregunta.html'
    success_url = reverse_lazy('lista_preguntas')

# editar pregunta
class PreguntaUpdateView(AdminRequeridoMixin, UpdateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'contenido/formulario/formulario_pregunta.html'
    success_url = reverse_lazy('lista_preguntas')

# eliminar pregunta
class PreguntaDeleteView(AdminRequeridoMixin, DeleteView):
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
class PerfilListView(AdminRequeridoMixin, ListView):
    model = Perfil
    template_name = 'contenido/lista/lista_perfiles.html'
    context_object_name = 'perfiles'

class PerfilCreateView(AdminRequeridoMixin, CreateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'contenido/formulario/formulario_perfil.html'
    success_url = reverse_lazy('lista_perfiles')

class PerfilUpdateView(AdminRequeridoMixin, UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'contenido/formulario/formulario_perfil.html'
    success_url = reverse_lazy('lista_perfiles')

class PerfilDeleteView(AdminRequeridoMixin, DeleteView):
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
class TipoAmenazaListView(AdminRequeridoMixin, ListView):
    model = TipoAmenaza
    template_name = 'contenido/lista/lista_amenazas.html'
    context_object_name = 'amenazas'

class TipoAmenazaCreateView(AdminRequeridoMixin, CreateView):
    model = TipoAmenaza
    form_class = TipoAmenazaForm
    template_name = 'contenido/formulario/formulario_amenaza.html'
    success_url = reverse_lazy('lista_amenazas')

class TipoAmenazaUpdateView(AdminRequeridoMixin, UpdateView):
    model = TipoAmenaza
    form_class = TipoAmenazaForm
    template_name = 'contenido/formulario/formulario_amenaza.html'
    success_url = reverse_lazy('lista_amenazas')

class TipoAmenazaDeleteView(AdminRequeridoMixin, DeleteView):
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
class MedioListView(AdminRequeridoMixin, ListView):
    model = Medio
    template_name = 'contenido/lista/lista_medios.html'
    context_object_name = 'medios'

class MedioCreateView(AdminRequeridoMixin, CreateView):
    model = Medio
    form_class = MedioForm
    template_name = 'contenido/formulario/formulario_medio.html'
    success_url = reverse_lazy('lista_medios')


class MedioUpdateView(AdminRequeridoMixin, UpdateView):
    model = Medio
    form_class = MedioForm
    template_name = 'contenido/formulario/formulario_medio.html'
    success_url = reverse_lazy('lista_medios')

class MedioDeleteView(AdminRequeridoMixin, DeleteView):
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
class OpcionListView(AdminRequeridoMixin, ListView):
    model = Opcion
    template_name = 'contenido/lista/lista_opciones.html'
    context_object_name = 'opciones'


class OpcionCreateView(AdminRequeridoMixin, CreateView):
    model = Opcion
    form_class = OpcionForm
    template_name = 'contenido/formulario/formulario_opcion.html'
    success_url = reverse_lazy('lista_opciones')

class OpcionUpdateView(AdminRequeridoMixin, UpdateView):
    model = Opcion
    form_class = OpcionForm
    template_name = 'contenido/formulario/formulario_opcion.html'
    success_url = reverse_lazy('lista_opciones')

class OpcionDeleteView(AdminRequeridoMixin, DeleteView):
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


# Dashboard de perfiles

class CuestionarioListView(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = 'contenido/cuestionario.html'
    context_object_name = 'perfiles'

    def get_queryset(self):
        return Perfil.objects.filter(activo=True).order_by('nombre')


class PreguntasPerfilView(LoginRequiredMixin, ListView):
    model = Pregunta
    template_name = 'contenido/preguntas_perfil.html'
    context_object_name = 'preguntas'

    def get_queryset(self):
        self.perfil = get_object_or_404(
            Perfil,
            slug=self.kwargs['slug'],
            activo=True
        )

        preguntas = Pregunta.objects.filter(
            perfil=self.perfil,
            activa=True
        ).annotate(total_opciones=Count('opciones')).filter(total_opciones=3)

        return [
            pregunta for pregunta in preguntas
            if pregunta.opciones.filter(es_correcta=True).count() == 1
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = self.perfil
        return context

# responder cuestionario

class ResponderPreguntaView(LoginRequiredMixin, View):
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

        return redirect('preguntas_perfil', slug=pregunta.perfil.slug)


# Registro de usuarios
class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'contenido/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
        return response


# Historial de respuestas del usuario
class HistorialView(LoginRequiredMixin, ListView):
    model = RegistroRespuesta
    template_name = 'contenido/historial.html'
    context_object_name = 'registros'

    def get_queryset(self):
        return RegistroRespuesta.objects.filter(usuario=self.request.user).select_related('pregunta', 'opcion').order_by('-fecha_respuesta')



# Guardar consentimiento de cookies
def guardar_consentimiento(request):

    if request.method == 'POST':

        decision = request.POST.get('decision')

        if decision in ['accepted', 'rejected']:

            destino = request.POST.get('next')

            if not url_has_allowed_host_and_scheme(
                url=destino,
                allowed_hosts={request.get_host()}
            ):
                destino = 'cuestionario'

            respuesta = redirect(destino)

            respuesta.set_cookie(
                'ciberduo_cookie_consent',
                decision,
                max_age=31536000,
                httponly=True,
                samesite='Lax',
                secure=request.is_secure()
            )

            return respuesta

    return redirect('cuestionario')


def cambiar_tema(request):
    if request.method == 'POST':
        tema = request.POST.get('theme')
        destino = request.POST.get('next')

        if tema not in ['light', 'dark']:
            return redirect('cuestionario')

        if not url_has_allowed_host_and_scheme(
            url=destino,
            allowed_hosts={request.get_host()}
        ):
            destino = 'cuestionario'

        respuesta = redirect(destino)
        respuesta.set_cookie(
            'ciberduo_theme',
            tema,
            max_age=31536000,
            httponly=True,
            samesite='Lax',
            secure=request.is_secure()
        )
        return respuesta

    return redirect('cuestionario')