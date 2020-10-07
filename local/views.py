from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse('Local')

# page for authentication 
def auth(request):
    return render(request, 'local/auth.html')


# page for adding or deleting any items from the  owners database
def edit(request):
    return render(request, 'local/editpage.html')


# page for all orders acceptance + calculate bills
def orders(request):
    return render(request, 'local/order.html')
