# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from time import gmtime, strftime
# Create your views here.

def index(request):
    if not 'list' in request.session:
        request.session['list'] = []
    print request.session['list']
    return render(request,'session_words/index.html')

def add(request):
    if request.method == "POST":
        word = request.POST['word']
        if len(word) < 1:
            messages.error(request, "Word can't be empty")
        if not "color" in request.POST:
            messages.error(request, "Choose a color")
        storage = get_messages(request)
        if storage:
            return redirect('/session_words')
        color = request.POST['color']
        font = "off"
        if "font" in request.POST:
            font = request.POST['font']
        
        request.session['list']+=[{
            "word": word,
            "color": color,
            "font": font,
            "time": strftime("%H:%M:%S%p %B %d %Y", gmtime())
            }]
        return redirect("/session_words")
    else:
        return redirect("/session_words")

def clear(request):
    if request.method == "POST":
        request.session['list'] = []
        return redirect("/session_words")
    else:
        return redirect("/session_words")