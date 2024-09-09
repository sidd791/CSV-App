from django.shortcuts import render
from app.tasks import add
from celery.result import AsyncResult
# Create your views here.
def index(request):
    result = add.delay(10,20)
    return render(request, 'layouts/home.html', {'result' : result})

def about(request):
    return render(request, 'layouts/about.html')

def contact(request):
    return render(request, 'layouts/contact.html')

def check_result(request, result_id):
    result = AsyncResult(result_id)
    return render(request, "layouts/check_result.html", {'result' : result  })