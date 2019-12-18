from django.http import HttpResponse
from django.shortcuts import render

#furits = {'apple':'apple is 100 per kg', 'mango':'mango is 80 per kg', 'banana':'banana is 40 per kg'}

def homepage(request):
    return render(request, 'home.html' )

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word == '--':
            continue
        elif word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    return render(request, 'count.html', {'fulltext': fulltext, 'wordlist': len(wordlist), 
                            'worddict': worddict })

def about(request):
    return render(request, 'about.html')
