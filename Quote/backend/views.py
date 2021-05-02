from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    quote =  "https://api.quotable.io/random"
    data = requests.get(quote).json()

    load_data ={'content': data['content'],
                'author': data['author']}

    context = {'load_data':load_data}
    template_name = "home.html"
    return render(request, template_name, context)