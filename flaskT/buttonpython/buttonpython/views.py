from django.shortcuts import render
import requests


def button(request):
    return render(request, 'html.html')

def output(request):
    data = requests.get("https://regres.in/api/users")
    print(data.text)
    data = dat.text
    return render(request, 'home.html', {'data':data})
