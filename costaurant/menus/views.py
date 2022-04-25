from django.shortcuts import render
from datetime import datetime
from menus.models import Menu


# Create your views here.
def index(request):
    context = {}
    today = datetime.now().date()
    menus = Menu.objects.all()
    context["today"] = today
    context["menus"] = menus
    return render(request, 'menus/index.html', context)


def detail(request, pk):
    context = {}
    menu = Menu.objects.get(id=pk)
    context["menu"] = menu
    return render(request, 'menus/detail.html', context=context)
