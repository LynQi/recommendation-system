# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import HttpResponse
from recommendation import models
from django.db import connection
from django.shortcuts import render_to_response


# Create your views here.

def index(request):
    if request.method == "POST":
        size = request.POST.get("size", None)
        gender = request.POST.get("gender", None)
        tmperature = request.POST.get("region", None)

        # return render(request, "index.html", {"data": id})
    return render(request, "index.html")
