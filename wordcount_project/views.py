from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    words=fulltext.split()
    worddictionary={}

    for i in words:
        if i in worddictionary:
            #increase
            worddictionary[i]+=1
        else:
            worddictionary [i]=1
        #add to worddictionary
    sorted_words=sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)
    wordcount=len(words)
    return render(request, 'count.html',{'fulltext':fulltext,'count':wordcount+1,'sorted_words':sorted_words})
t