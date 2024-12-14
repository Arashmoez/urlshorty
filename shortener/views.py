from django.shortcuts import render , redirect
from .models import MoezUrl

# Create your views here.
def shortener_detail_view(request , string):
    obj = MoezUrl.objects.get(shortcode=string)
    return redirect(f"https://{obj.url}")

