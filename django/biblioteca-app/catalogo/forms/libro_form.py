from django import forms
from catalogo.models import Libro


class Libroform(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autores', 'fecha_publicacion', 'categoria', 'isbn']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.CheckboxSelectMultiple(),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        }
