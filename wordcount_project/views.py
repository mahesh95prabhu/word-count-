from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

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
    send_mail(
    subject = "Email from workstation,
    message = "This is a test email",
    from_email = 'max@workstation',   # This will have no effect is you have set DEFAULT_FROM_EMAIL in settings.py
    recipient_list = ['max@k8scluster.com'],    # This is a list
    fail_silently = False     # Set this to False so that you will be noticed in any exception raised
    )
    return render(request, 'count.html',{'fulltext':fulltext,'count':wordcount+1,'sorted_words':sorted_words})
