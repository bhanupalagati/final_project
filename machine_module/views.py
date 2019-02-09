from django.shortcuts import render
from django.http import HttpResponse
from machine_module.forms import dataInput_form
from machine_module import pickle
import numpy as np

# Create your views here.
def index(request):
    return render(request,'index.html')


def dataInputRequest(request):

    form = dataInput_form()

    if request.method == "POST":
        form = dataInput_form(request.POST)
        data_Input = request.POST
        article = data_Input.__getitem__('data')
        if form.is_valid():
            form.save(commit=True)
            return analyser(request,article)
        else:
            print("Form validation Failed")
    return render(request,"dataform.html",{'form':form})

def analyser(request,article):
    article = np.array(article)
    val = pickle.prediction(article)
    dic = {'res' : val}
    return render(request,'prediction.html',context=dic)
