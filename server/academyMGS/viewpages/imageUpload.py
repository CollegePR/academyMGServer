from academyMGS.models import *
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from ..forms import ImageUploadForm


def imageUpload(request):
    data = {'flag': False}
    image = ""
    #image = image.cleaned_data['image'],
    if request.method == "POST":
        image = ImageUploadForm(request.POST, request.FILES)
    else:
        return HttpResponse(json.dumps(data), content_type='application/json')
    print(image)
    value = Student.objects.order_by('-pk')[0]
    jungsungwookbyeongsin = image.cleaned_data
    print(jungsungwookbyeongsin)
    value.image = jungsungwookbyeongsin['image']
    value.save()
    data = {'flag': True}
    return HttpResponse(json.dumps(data), content_type='application/json')