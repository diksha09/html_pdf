from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.http import HttpResponse
from django.views.generic import View
from django.template import loader
 
from django.template.loader import get_template
 
from .utils import render_to_pdf 

# def data(request):
#    s = []
#    for i in range (1000):
#       s.append(i)
  
   
#    return render(request, 'core/invoice.html', {'s':s} )

 
class GeneratePdf(View):
   def get(self, request, *args, **kwargs):
        
      pdf = render_to_pdf('core1/invoice.html')
         
      response =  HttpResponse(pdf, content_type='application/pdf')
      response['Content-Disposition'] = 'inline'
      return response
        

