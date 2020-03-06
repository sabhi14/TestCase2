from django.shortcuts import render
from .models import AccountDetails
from django.http import HttpResponse
from django.template import loader

def home(request):
        allAccountDetails = AccountDetails.objects.all()
        container = {
                'allAccountDetails' : allAccountDetails,
        }
        print(str(allAccountDetails))
        template = loader.get_template('catalog/index.html')
        return HttpResponse(template.render(container, request))

def 