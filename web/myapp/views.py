from django.shortcuts import render, HttpResponse

# Create your views here.


def Hello_html(request):
    return render(request, 'todos/home.html')

def post_example(request):
    name = 