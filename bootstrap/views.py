# in Porg 8 :- Put POST instead of GET to put msg in body instead of open(seen in url so no privacy)
# also check charage in newline remover
# put POST index.html action file also
# Also put CSRF token
# from edit prog 8 make prog 9

# from edit prog 9 make prog 10
# make IF instead of ELIF
# Remove return render from all removepunc, upper, extraspace and put in last line
# Add djtext = analyzed in all function except last (no need in last)
# delete Else Statement

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index2.html")


# PROGRAM - 5 (2nd Method)
# Extra space remover

def analyze(request):
    # Get the Text
    djtext = request.POST.get('text', 'default')

    # Check checkBox Value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check with checkBox
    if (removepunc == "on"):
        # Analyze djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'extra space remvoe', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ''
        # also check charage(char) return for new line remover
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Please select any operation and try again!")

    return render(request, 'analyze.html', params)
