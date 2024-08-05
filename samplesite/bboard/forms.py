from django import forms
from .models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Название должно быть не менее 5 символов.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Описание должно быть не менее 10 символов.")
        return description
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if not text:
            raise forms.ValidationError("Комментарий не может быть пустым.")
        if len(text) < 5:
            raise forms.ValidationError("Комментарий должен содержать не менее 5 символов.")
        return text

