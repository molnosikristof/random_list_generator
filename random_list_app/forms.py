from django import forms

class NameForm(forms.Form):
    list_name = forms.CharField(label='List name', max_length=100)
    list_content = forms.CharField(label='List content', max_length=1000)
