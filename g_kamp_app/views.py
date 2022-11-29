from django.shortcuts import render
from django.http import HttpResponse

def check(reqest):
    return HttpResponse('Hello')

