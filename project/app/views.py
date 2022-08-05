from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import urllib.request as urllib2
from urllib.request import urlopen
import json
from .models import Repository


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

             # def remove(string):
             #     return string.replace(" ", "")

             for document in response['response']['docs']:
                 doc.append(document['attr_stream_name'])
                 # id.append(document['id'])

             hi=[]

             for names in doc:
                 hi.append(names[0])


             # print(id)
             # print(hi)


             context = {

                 "name": hi,
                 # "ids": id,
             }

             return render(request,'basic.html', context)
    return render(request,'basic.html')


def Repo(request):
  info = Repository.objects.all()

  return render(request,'app/repository.html', {'gett':info})
