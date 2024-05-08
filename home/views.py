from django.shortcuts import render

def home(request):
    peoples = [
        {'Name': 'ayush', 'age': 18},
        {'Name': 'ayush', 'age': 18},
        {'Name': 'ayush', 'age': 18},
    ]
    return render(request, "index.html", context={'peoples': peoples, "title": 'Django'})
