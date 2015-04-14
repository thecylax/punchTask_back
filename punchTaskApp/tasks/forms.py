from django import forms

from punchTaskApp.tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Task name',
                    'class':'col-md-12 form-control'
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'placeholder':'Enter a description',
                    'class':'form-control'
                }
            ),
        }
