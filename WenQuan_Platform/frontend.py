#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
This is for frontend router navigation
All urls that doesn't conform to backend url patterns will be dealt with here
'''
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .settings import STATICFILES_DIRS

def index(request, url):
    '''
    if 'static' or 'img' or 'manifest' is found, redirect them to static files,
    else, let frontend(index.html) deal with them
    '''
    url = request.path
    keywords = ("static", "img", "manifest.json")
    for keyword in keywords:
        pos = url.find(keyword)
        if pos != -1:
            return HttpResponseRedirect("/frontend/"+url[pos:])
    not_allow_redirect_keywords = ("service-worker", "precache")
    for keyword in not_allow_redirect_keywords:
        pos = url.find(keyword)
        if pos != -1:
            content = open(STATICFILES_DIRS[0] + "/" + url[pos:]).read()
            return HttpResponse(content, content_type="text/javascript")
    return render(request, "index.html")
