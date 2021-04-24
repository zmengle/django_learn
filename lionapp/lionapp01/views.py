from django.shortcuts import render
from lionapp01.models import Logs

# Create your views here.


def selectLog(request):
    log = Logs.objects.all()
    context = {'log': log}
    return render(request, 'logs.html', context)
