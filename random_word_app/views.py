from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string


def random_word(request):
    context = {
        'try_count': get_random_string(length=14)
    }
    return render(request, "display.html", context)

# def counting_page(request):
#     context = {
#         'context': request.session['context'],
#     }
    
#     return render (request, "display.html", context)

def return_page(request):
    if request.method == "GET":
        return redirect('/new_page')
    # # counter = 0
    # # counter += 1
    # request.session['stuff']= {
    #     'counter': int(counter),
    #     'try_count': get_random_string(length=14)
    #     }
    return redirect('/new_page')

def new_page(request):
    print ('reached page!')
    counter = 0
    counter += 1
    context = {
        'counter': int(counter),
        'try_count': get_random_string(length=14)
        }
    return render(request, "display.html", context)
    # return redirect('/random_word', context)
    


# def some_function(request):
#     if request.method == "GET":
#         return redirect('/')
#     request.session['result'] = {
#         'name': request.POST['name'],
#         'language': request.POST['language'],
#         'location': request.POST['location'],
#         'gender': request.POST['gender'],
#         'description': request.POST['description'],
#         }
#     return redirect('/result')

# def result(request):
#     context = {
#         'result': request.session['result'],
#     }
#     return render(request, "other.html", context)
    
    