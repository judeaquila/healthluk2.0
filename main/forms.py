from django.forms import ModelForm
from .models import Waitlist

class WaitlistForm(ModelForm):
    class Meta:
        model = Waitlist
        fields = ['email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your Email to Join our Waitlist'})