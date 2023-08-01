from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.models import *
from app.forms import *
# Create your views here.

#~ This is a Student Form Funtion based View using which we will insert data
def functionBasedView_SF(request):
    SFO = StudentForm(label_suffix='')
    d = {'SFO': SFO}
    if request.method == 'POST':
        SFD = StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('<center><h2 style="font-family:Arial;">Data Inserted Successfully</h2></center>')
    return render(request,'functionBasedView_SF.html',d)
    
#~ This is a Student Form Class Based View using which we will insert data
class ClassBasedView_SF(View):
    #-----get method for retrieving the data 
    def get(self, request):
        SFO = StudentForm(label_suffix='')
        d = {'SFO':SFO}
        return render(request,'ClassBasedView_SF.html',d)
    #-----post method ..when post method is activate
    def post(self, request):
        SFD = StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('<center><h2 style="font-family:Arial;">Data Inserted Successfully</h2></center>')

#~ This is an Example of TemplateView
class Template_View(TemplateView):
    template_name = 'Template_View.html'