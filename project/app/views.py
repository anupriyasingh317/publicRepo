from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import urllib.request as urllib2
from urllib.request import urlopen
import json
import os

@method_decorator(csrf_exempt, name='dispatch')
@csrf_exempt
def basic(request):
    if request.method=='POST':
        if request.POST['form_type'] == 'click_button':
             data = request.POST.get('name','')
             string = "http://localhost:8983/solr/test/select?q=cheese&wt=json"
             if (data.isspace() == False):
                 a = data.replace(" ", "%20")
                 link = string.replace("cheese", a)
             else:
                 link = string.replace("cheese", data)
             connection = urlopen(link)
             response = json.load(connection)
             print(response['response']['numFound'], "documents found.")

             doc=[]

             def remove(string):
                 return string.replace(" ", "")

             for document in response['response']['docs']:
                 doc.append(document['attr_stream_name'])

             # print(doc)
             hi=[]
             for names in doc:
                 hi.append(names[0])
             print(hi)

             #print(hi[0].replace("[","").replace("]",""))

             return render(request,'basic.html',{"name": hi})
    return render(request,'basic.html')