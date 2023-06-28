from django.forms import ModelForm, TextInput, EmailInput,  Textarea

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Your username'}),
            'email': EmailInput(attrs={'placeholder': 'Your email'}),
            'message': Textarea(attrs={'placeholder': 'Your query', 'rows': 10, 'cols': 30})
        }
