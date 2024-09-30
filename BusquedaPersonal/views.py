from django.http import JsonResponse
from django.shortcuts import render
from .models import PersonasModelo
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import EditarPersonaForm

def personas_list(request):
    personas = PersonasModelo.objects.values('dni', 'nombre', 'apellidos').order_by('apellidos')
    return render(request, 'personas_list.html', {'personas': personas})

def personas_filtrar(request):
    search_term = request.GET.get('search', '')
    personas = PersonasModelo.objects.filter(
        Q(apellidos__icontains=search_term) | Q(nombre__icontains=search_term)
    ).values('dni', 'nombre', 'apellidos').order_by('apellidos')
    return JsonResponse(list(personas), safe=False)

class EditarPersonaView(UpdateView):
    model = PersonasModelo
    form_class = EditarPersonaForm
    template_name = 'personapag.html'
    success_url = reverse_lazy('personas_list')
    pk_url_kwarg = 'dni'
    def form_valid(self, form):
        print("Formulario válido, guardando...")
        return super().form_valid(form)
    def form_invalid(self, form):
        print("Errores en el formulario:", form.errors)  # Esto te ayudará a ver qué está fallando
        return super().form_invalid(form)

