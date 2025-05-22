from itertools import chain
from urllib import response
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseBadRequest
import os
from dotenv import load_dotenv
import google.generativeai as genai
from .models import * 

# Create your views here.
def home(request):
    api_key = os.get_env('GOOGLE_API_KEY')
    if not api_key:
        # HttpResponseBadRequest()
        pass 
    genai.configure(api_key = api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(Chat.question)
    Chat.answer = response
    return render(request, home.html)
