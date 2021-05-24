from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string


def random_word(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['try_count'] = get_random_string(length=14)
    request.session['counter'] += 1
    return render(request, "display.html")
    # context = {
    #     'try_count': get_random_string(length=14)
    # }
    # return render(request, "display.html", context)

def return_page(request):
    if request.method == "GET":
        return redirect('/new_page')
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

def reset(request):
    request.session.flush()
    return redirect('/random_word')
    