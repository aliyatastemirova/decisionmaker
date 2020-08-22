from django import forms


class Question(forms.Form):
    question = forms.CharField(required=True,
                               max_length=100,
                               min_length=2,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': "My question..."
                               }))


class Answers(forms.Form):
    answer = forms.CharField(label='Answer', required=True,
                             max_length=100,
                             min_length=2,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': "My option..."
                             }))
