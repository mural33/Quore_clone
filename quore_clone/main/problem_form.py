from django import forms

class ProblemForm(forms.Form):
    title = forms.EmailField(label='title')
    description = forms.EmailField(label='description',widget=forms.Textarea)
