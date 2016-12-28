from django.shortcuts import render
from django.core.paginator import Page




def main(request):
    '''
    Render the main Page
    '''
    return render(request, 'main/main.html',)

def homepage(request):
    '''
    Render the homepage Page
    '''
    return render(request, 'main/homepage.html',)