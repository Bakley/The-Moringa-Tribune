from django import forms
from .models import Article


class NewsLetterForm(forms.Form):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
