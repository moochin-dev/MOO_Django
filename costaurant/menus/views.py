from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'menus/index.html')

def detail(request, menu):
    context = {"menu": menu}
    return render(request, "menus/detail.html", context = context)