from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from dictionary.models import Dictionary

# ========================
# Show entry form
# ========================
def enter(request):
    return render(request, "dictionary.html")

# ========================
# Add word entry to database
# ========================
def enter2(request):
    if request.method == "POST":
        word_entry = request.POST.get("word_entry")
        word_meaning = request.POST.get("word_meaning")

        if not word_entry or not word_meaning:
            return HttpResponseBadRequest("Both fields are required.")

        # Only save if it doesn't exist
        if not Dictionary.objects.filter(word_entry__iexact=word_entry).exists():
            Dictionary.objects.create(word_entry=word_entry, word_meaning=word_meaning)

        return render(request, "dictionary2.html")

# ========================
# Search for a word
# ========================
def enter3(request):
    if request.method == "POST":
        word = request.POST.get("word_query")

        # Get only the first matching entry
        searchdata = Dictionary.objects.filter(word_entry__iexact=word).distinct('word_entry')

        return render(request, 'result.html', {'searchresult': searchdata})
