from django import forms
from .models import Traveller

# class TravellerForm(forms.ModelForm):
#     """
#     Form class for users to create their Traveller profile
#     """
#     class Meta:
#         model = Traveller
#         # firstname = forms.CharField()
#         # lastname = forms.CharField()
#         # bio = forms.CharField()
#         profile_photo = forms.ImageField()
#         fields = ('firstname', 'lastname', 'bio', 'profile_photo')
#         # fileFields = ('profile_photo',)
#         # # profile_photo = forms.FileField()

class TravellerForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea(attrs={'type': 'text','rows': 4, 'cols': 40}))
    profile_photo = forms.ImageField()