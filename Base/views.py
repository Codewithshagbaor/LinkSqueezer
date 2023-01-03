from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from . models import Link
import uuid
from decouple import config
# Create your views here.
def index(request):
  links = Link.objects.all()
  response_data = {}

  if request.POST.get('action') == 'post':
    link = request.POST.get('link')
    uid = str(uuid.uuid4())[:5]

    response_data['link'] = link
    response_data['uid'] = uid

    Link.objects.create(
      uid = uid,
      link = link,
    )
    return JsonResponse(response_data)
  return render(request, 'index.html', {'links':links})

def linkView(request, uid):
  link = get_object_or_404(Link, uid=uid)
  
  # RECAPTCHA_SITE_KEY = config('RECAPTCHA_SITE_KEY')
  # RECAPTCHA_SECRET_KEY=config('RECAPTCHA_SECRET_KEY')
  context = {
    'link':link
  }
  return render(request, 'redirect.html', context)