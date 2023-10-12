from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'full_text', 'date']
        
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mt-3',
                "placeholder": "Название статьи"
                }),
            "intro": TextInput(attrs={
                'class': 'form-control mt-3',
                "placeholder": "Анонс"
                }),
            "full_text": Textarea(attrs={
                'class': 'form-control mt-3',
                "placeholder": "Текст статьи"
                }),
            "date": DateTimeInput(attrs={
                'class': 'form-control mt-3',
                'name': 'date',
                "placeholder": "Дата публикации"
                }),
            # "date": TextInput(attrs={'class': 'form-control mt-3', 'type': 'time', 'name': 'time'}),
        }