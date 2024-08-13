from django import forms
from .models import Post, Category, Quote
from django.forms import ModelForm
from django import forms
from .models import *
from .widget import MoodWidget



class PostForm(forms.ModelForm):
    mood = forms.IntegerField(
    widget=MoodWidget()
    )

    class Meta:
        model = Post
        fields = ['title','content','date_posted','author','categories','mood']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter the title'
            }),
            'content': forms.Textarea(attrs={
                'rows': 5,
                'cols': 5,
                'class': 'form-control', 
                'placeholder': 'Enter the content'
            }),
            'date_posted':forms.SelectDateWidget(attrs={
                'class': 'form-control',
                'row':'1','col':'1 ',
                'placeholder': 'YYYY-MM-DD'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Author name'
            }),
            'categories': forms.SelectMultiple(attrs={
                'class': 'form-control'
            })
            }
        day = forms.DateField(
        initial=timezone.now,
        widget=forms.SelectDateWidget(attrs={'class': 'form-control', 'row':'1','col':'1','placeholder': 'YYYY-MM-DD'}))


class create_cat(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'quote']
        widgets = {
            'author': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'enter the author'
            }),
            'quote': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter the quote'
            })
        }



