#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
This is for frontend router navigation
All urls that doesn't conform to backend url patterns will be dealt with here
'''
from django.shortcuts import render, redirect

def index(request, url):
    '''
    if 'static' or 'img' or 'manifest' is found, redirect them to static files,
    else, let frontend(index.html) deal with them
    '''
    url = request.path
    keywords = ("static", "img", "manifest")
    for keyword in keywords:
        pos = url.find(keyword)
        if pos != -1:
            return redirect("/frontend/"+url[pos:])
    return render(request, "index.html")
