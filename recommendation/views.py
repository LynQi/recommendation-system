# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import HttpResponse
from recommendation import models
from django.db import connection
from django.shortcuts import render_to_response


# Create your views here.
testee = []
flag = 0

def index(request):
    global flag
    if request.method == "POST":
        pw = request.POST.get("password", None)
        if pw == 'EverlastingRecommendation': 
            flag = 1
            return render(request, "classA.html")
        else:
            return render(request, "login.html")
    elif request.method == "GET":
        flag = 0
        return render(request, "login.html")
    else:
        return render(request, "login.html")

def classA(request):
    if flag == 1:
        if request.method == "POST":
            size = request.POST.get("size", None)
            gender = request.POST.get("gender", None)
            tmperature = request.POST.get("region", None)
            return render(request, "classA.html")
        else:
            return render(request, "classA.html")
    else:
        return render(request, "login.html")

def classB(request):
    if flag == 1:
	    if request.method == "POST":
	        if request.POST.get("number", None):
	            n = request.POST.get("number", None)
	            n = int(n)
	            for i in range(len(testee)):
	                if testee[i]['num'] == n:
	                    del testee[i]
	                    break
	        else:
	            pid = request.POST.get("product", None)
	            fr = request.POST.get("fit", None)
	            sr = request.POST.get("style", None)
	            tmp = {'productid': pid, 'fitrating': fr, 'stylerating':sr, 'num': len(testee)}
	            testee.append(tmp)
	        return render(request, "classB.html", {"data": testee})
	    elif request.method == "GET":
	        testee.clear()
	        return render(request, "classB.html")
	    else:
	        return render(request, "classB.html",{"data": testee})
    else:
	    return render(request, "login.html")
