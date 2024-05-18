from django.http import HttpResponse
from django.shortcuts import render
from .models import Member
from django.template import loader
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('profile.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
