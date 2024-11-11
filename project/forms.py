from django import forms 
from .models import Project

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('year', 'map', 'address', 'document', 'name', 'category', 'project_cost', 'status', 'started', 'contact', 'description', 'update',)

        widgets = {
            'year': forms.Select(attrs={'class': INPUT_CLASSES}),
            'map': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'document': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'project_cost': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'status': forms.Select(attrs={'class': INPUT_CLASSES}),
            'started': forms.DateInput(attrs={'class': INPUT_CLASSES, 'type': 'date'}),
            'contact': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'update': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'address': forms.TextInput(attrs={'class': INPUT_CLASSES}),
        }

class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('year', 'name', 'document', 'project_cost', 'status', 'started', 'contact', 'description', 'update', 'address',)

        widgets = {
            'year': forms.Select(attrs={'class': INPUT_CLASSES}),
            'map': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'document': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'project_cost': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'status': forms.Select(attrs={'class': INPUT_CLASSES}),
            'started': forms.DateInput(attrs={'class': INPUT_CLASSES, 'type': 'date'}),
            'contact': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'update': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'address': forms.TextInput(attrs={'class': INPUT_CLASSES}),
        }