import base64
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView
from .models import PersonasModelo, VidaLaboral
from .forms import EditarPersonaForm


class PersonasListView(ListView):
    model = PersonasModelo
    template_name = 'personas_list.html'
    context_object_name = 'personas' 

    def get_queryset(self):
        return PersonasModelo.objects.filter(no_persona=False).values('dni', 'nombre', 'apellidos').order_by('apellidos')

def personas_filtrar(request):
    search_term = request.GET.get('search', '')
    personas = PersonasModelo.objects.filter(
        Q(apellidos__icontains=search_term) | Q(nombre__icontains=search_term),
        no_persona=False 
    ).values('dni', 'nombre', 'apellidos').order_by('apellidos')
    return JsonResponse(list(personas), safe=False)

class EditarPersonaView(UpdateView):
    model = PersonasModelo
    form_class = EditarPersonaForm
    template_name = 'personapag.html'
    success_url = reverse_lazy('personas_list')
    pk_url_kwarg = 'dni'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        persona = self.get_object()
        context['persona'] = persona

        # Convertir la imagen a base64
        if persona.foto:
            
            if persona.foto and isinstance(persona.foto, bytes):
        
                context['persona'].foto = f"data:image/jpeg;base64,{base64.b64encode(persona.foto).decode('utf-8')}"

        return context

    def form_valid(self, form):
        print("Formulario válido, guardando...")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Errores en el formulario:", form.errors)
        return super().form_invalid(form)
    
class VidaLaboralView(ListView):
    model = VidaLaboral
    template_name = 'vidalaboral.html'
    context_object_name = 'vida_laboral'

    def get_queryset(self):
        dni = self.kwargs['dni']
        persona = get_object_or_404(PersonasModelo, dni=dni)
        return VidaLaboral.objects.filter(persona=persona)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persona'] = get_object_or_404(PersonasModelo, dni=self.kwargs['dni'])
        return context
