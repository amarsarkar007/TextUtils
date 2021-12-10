#i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')  ##index.html--textarea--name--text
    #check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # charcount = request.GET.get('charcount', 'off')

    purpose = ""
    
    # print(djtext)
    # print(removepunc)
    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyze=""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char

        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyze}
        purpose += " | Remove Punctuations"

        djtext=analyze
        # return render(request,'analyze.html', params)

    if(fullcaps == "on"):
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()

        params = {'purpose':'change to uppercase', 'analyzed_text':analyze}
        purpose += " | change to uppercase"

        djtext=analyze
        # return render(request,'analyze.html', params)

    if(newlineremover == "on"):
        analyze = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyze = analyze + char
        params = {'purpose':'Remove new lines', 'analyzed_text':analyze}
        purpose += " | Remove new lines"
        djtext=analyze
        # return render(request,'analyze.html', params)   

    if(extraspaceremover == "on"):
        analyze = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyze = analyze + char
        params = {'purpose':'Remove extra Space', 'analyzed_text':analyze}
        purpose += " | Remove extra Space"
        djtext=analyze

        # return render(request,'analyze.html', params)

    # elif(charcount == "on"):
    #     analyze = {}
    #     for char in djtext:
    #         analyze[char] = djtext.upper.count(char)

    #     params = {'purpose':'Remove extra Space', 'analyzed_text':analyze}
    #     return render(request,'analyze.html', params)

 
    if(removepunc != "on" and fullcaps != "on" and newlineremover !="on" and extraspaceremover !="on"):
        return HttpResponse("Error")

    params ={'purpose':purpose, 'analyzed_text':analyze}


    return render(request,'analyze.html', params)

