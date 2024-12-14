from .models import MoezUrl
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class MoezUrlForm(ModelForm):
    class Meta:
        model = MoezUrl
        fields = ['url' , 'shortcode']


