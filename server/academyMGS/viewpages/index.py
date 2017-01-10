from academyMGS.models import *
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
def index(request):
    return HttpResponse("don't access", content_type='application/json')