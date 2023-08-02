from typing import Any, Dict
from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from django.http import HttpResponse
from App.forms import *

class TemplateData(TemplateView):
    template_name='TemplateData.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['name']='Narasimha'
        return context
    
class TempViewForm(TemplateView):
    template_name='TempViewForm.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context=super().get_context_data(**kwargs)
        SFO=StudentForm()
        context['SFO']=SFO
        return context
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('<center><h1><b> Data Inserted Successfully </b></h1></center>')
    
class FormViewForm(FormView):
    template_name='FormViewForm.html'
    form_class = StudentForm
    success_url='/success/'
    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return HttpResponse('<center><h1><b> Data Inserted Successfully </b></h1></center>')
