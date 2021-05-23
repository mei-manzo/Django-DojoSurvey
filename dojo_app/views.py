from django.shortcuts import render, redirect, HttpResponse

def index(request):
    print('got here from redirect') #start here, post to /result (some_function), redirect to this_function
    return render(request, "index.html")

def some_function(request):
    if request.method == "POST":
        context = {
            'name': request.POST['name'],
            # 'language': request.POST['language'],
            # 'location': request.POST['location'],
            # 'gender': request.POST['gender'],
            # 'description': request.POST['description'],
        }
        # return render(request, "other.html", context)
        return redirect('this_function')
    return redirect('this_function')

def this_function(request):
    request.session['name'] = request.POST['name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    request.session['gender'] = request.POST['gender']
    request.session['description'] = request.POST['description']
    request.session['counter'] = 100
    return render(request, "other.html")
    
    

