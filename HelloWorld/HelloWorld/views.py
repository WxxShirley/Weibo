from django.shortcuts import render
from . import data_utils
from . import tools

wb=data_utils.WeiboCrawler('1740197697')
# wb.start()

def index(request):
    # wb=data_utils.WeiboCrawler('1740197697')
    # wb.start()
    context = tools.get_data()

    return render(request, 'index.html', context)

def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['name']='何晓昕'
    return render(request, 'runoob.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def intro(request):
    context = {}
    return render(request, 'intro.html', context)




