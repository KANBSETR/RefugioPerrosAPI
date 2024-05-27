from django.forms import ModelForm
from .models import Perro

class PerroForm(ModelForm):
    class Meta:
        model = Perro
        fields = ['nombre', 'raza', 'edad', 'descripcion']
        