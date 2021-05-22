from django.shortcuts import render, redirect, HttpResponse
def index(request):
    return render(request, "index.html")

def some_function(request):
    if request.method == "POST":
        context = {
            'name': request.POST['name'],
            'language': request.POST['language'],
            'location': request.POST['location'],
            'gender': request.POST['gender'],
            'description': request.POST['description'],
        }
        return render(request, "other.html", context)
    return render(request, "other.html")
