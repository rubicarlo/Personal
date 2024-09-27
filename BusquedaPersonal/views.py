from django.http import JsonResponse
from django.shortcuts import render
from .models import PersonasModelo
from django.db.models import Q

def personas_list(request):
    personas = PersonasModelo.objects.values('dni', 'nombre', 'apellidos').order_by('apellidos')
    return render(request, 'personas_list.html', {'personas': personas})

def personas_filtrar(request):
    search_term = request.GET.get('search', '')
    personas = PersonasModelo.objects.filter(
        Q(apellidos__icontains=search_term) | Q(nombre__icontains=search_term)
    ).values('dni', 'nombre', 'apellidos').order_by('apellidos')
    return JsonResponse(list(personas), safe=False)

