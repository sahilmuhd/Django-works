from django.shortcuts import render
from django.http import HttpResponse
from dictionary.models import Dictionary
# Create your views here.

def enter(request):
    return render(request,"dictionary.html")

def enter2(request):
    word_entry = request.POST.get("word_entry")
    word_meaning = request.POST.get("word_meaning")
    Dictionary.objects.create(word_entry=word_entry,word_meaning=word_meaning)
    
    return render(request,"dictionary2.html")
def enter3(request):
    word=request.POST.get("word_query")
    searchdata = Dictionary.objects.filter(word_entry=word)
    return render(request,'result.html',{'searchresult':searchdata})


