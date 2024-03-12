from django import forms
from .models import Traveller

class TravellerForm(forms.ModelForm):
    """
    Form class for users to create their Traveller profile
    """
    class Meta:
        model = Traveller
        fields = ('firstname', 'lastname', 'bio', 'profile_photo',)