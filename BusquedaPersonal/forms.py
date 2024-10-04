from django import forms
from .models import PersonasModelo

class EditarPersonaForm(forms.ModelForm):
    class Meta:
        model = PersonasModelo
        fields = [
            'dni', 'apellidos', 'nombre', 'externo',# 'responsable', 'cientifico', 
            'baja', 'directorio', 
            'nif', 'nie', 'nrp', 'nss', 'sexo', 'fecha_nacimiento', 'pais_nacimiento', 
            'mail_institucional', 'mail_alternativo', 'telefono_personal_fijo', 
            'telefono_personal_movil', 'codigo_postal', 'domicilio', 
            'localidad_domicilio', 'provincia_domicilio', 'foto'
        ]
        widgets = {
            'nif': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'nie': forms.TextInput(attrs={'class': 'form-control'}),
            'nrp': forms.TextInput(attrs={'class': 'form-control'}),
            'nss': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'},format='%Y-%m-%d'),
            'pais_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'directorio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
            'baja': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            'externo': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            'telefono_personal_fijo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_personal_movil': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(choices=[('M', 'Masculino'), ('F', 'Femenino')], attrs={'class': 'form-select'}),
            'mail_institucional': forms.EmailInput(attrs={'class': 'form-control'}),
            'mail_alternativo': forms.EmailInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad_domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'provincia_domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

class BuscarPersonaForm(forms.Form):
    query = forms.CharField(
        label='Buscar',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )