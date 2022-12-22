from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=40)
    sender = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)

