import operator

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'hithere':"This is Home page variable"})


def count(request):
    fulltext=request.GET['fulltext']
    #print(fulltext)
    wordlist = fulltext.split()
    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            #increase number
            worddictionary[word] += 1
        else:
            #add to dictionary
            worddictionary[word] = 1

    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'countedwords':sortedwords})



def about(request):
    return render(request, 'about.html')

