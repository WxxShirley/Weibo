from django.shortcuts import render
from . import data_utils

wb=data_utils.WeiboCrawler('1740197697')
# wb.start()


def index(request):
    # wb=data_utils.WeiboCrawler('1740197697')
    # wb.start()
    context = {}

    context['user_id']=wb.user_id

    context['关键词']=wb.keywors
    print(wb.keywors)

    return render(request, 'index.html', context)

def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['name']='何晓昕'
    return render(request, 'runoob.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)




