from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from models import HomePage
import logging

def home(request):
    try:
        homepage = get_object_or_404(HomePage, is_homepage=True)
        return render_to_response('index.html',
                {'homepage':homepage},context_instance=RequestContext(request))
    except Exception, e:
        print 'error: {0}'.format(e)

