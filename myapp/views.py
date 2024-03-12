from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def home(request):
  return HttpResponse("<h1>Hello Django!</h1>")

def about(request):
  return HttpResponse("<h1>About Page</h1>")

def function_view(request):
    context = {
        'page_title': 'Function-Based View',
        'page_heading': 'Welcome to the Function-Based View',
        'page_content': 'This is the content generated by the function-based view.',
    }
    return render(request, 'bootswatch.html', context)

class ClassView(View):
    def get(self, request):
        context = {
            'page_title': 'Class-Based View',
            'page_heading': 'Welcome to the Class-Based View',
            'page_content': 'This is the content generated by the class-based view.',
        }
        return render(request, 'bootswatch.html', context)
  
