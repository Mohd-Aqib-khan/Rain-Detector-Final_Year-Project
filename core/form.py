from dataclasses import field
from pyexpat import model
from django import forms
# from matplotlib.pyplot import cla
from core.models import Contact


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields=['name','email','subject','message']
#         widgets = {
# 	            "name": forms.TextInput(attrs={"class": "contact_input contact_input_name inpt","placeholder":"Your Name"}),
# 	            "email": forms.TextInput(attrs={"class": "contact_input contact_input_email inpt","placeholder":"Your E-mail"}),
# 	            "subject": forms.TextInput(attrs={"class": "contact_input contact_input_subject inpt","placeholder":"Subject"}),
# 	            "message": forms.Textarea(attrs={"class": "contact_textarea contact_input inpt","placeholder":"Message"}),
	            
	
#         }