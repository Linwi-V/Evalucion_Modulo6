from django import forms

class TareaForm(forms.Form):
    titulo = forms.CharField(
        max_length=200,
        label='Título',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: Comprar pan'
        })
    )
    descripcion = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Describe tu tarea aquí...'
        })
    )