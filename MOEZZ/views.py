from django.views import View
from django.shortcuts import render
from shortener.forms import MoezUrlForm
from shortener.models import MoezUrl
class HomeView(View):
    def get(self , request , *args , **kwargs):
        form = MoezUrlForm()
        context = {
            "form" : form
        }
        return render(request , "home.html" , context)
    def post(self , request , *args , **kwargs):
        flag = False
        form = MoezUrlForm(request.POST)
        context = {
            "form" : form
        }
        if form.is_valid():
            form.save()
            url = form.cleaned_data.get("url")
            qs = MoezUrl.objects.filter(url=url)
            count = qs.count()
            shortcode = form.cleaned_data.get("shortcode")
            flag = True
            context.update(url=url , shortcode=shortcode , flag=flag , count=count)
    
        return render(request , "home.html" , context)