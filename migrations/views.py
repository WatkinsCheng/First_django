from django.shortcuts import HttpResponse
from django.shortcuts import render


def index(request):
    # 封装字符串
    # return HttpResponse("Hello World!")

    return render(request, "index.html", )