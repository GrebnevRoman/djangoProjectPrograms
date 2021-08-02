from .models import Programs
from django.forms import ModelForm, TextInput


class ProgramForm(ModelForm):
    class Meta:
        model = Programs
        fields = ['Name', 'Specialty', 'Dep', 'General_hours', 'Code', 'Classroom_hours', 'Type']

        widgets = {
            "Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название программы'
            }),
            "General_hours": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Общее колличество часов'}),
            "Code": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код программы'}),
            "Classroom_hours": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Аудиторное колличество часов'}),
            "Type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип программы'})
        }
#
# }
