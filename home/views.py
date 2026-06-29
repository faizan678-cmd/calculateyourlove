from django.shortcuts import render
from .models import LoveCalculation
import random

def index(request):
    result = None
    if request.method == 'POST':
        your_name = request.POST.get('your_name')
        her_name  = request.POST.get('her_name')
        result    = random.randint(1, 100)

        # DB mein save karo
        LoveCalculation.objects.create(
            your_name=your_name,
            her_name=her_name,
            result=result
        )

    return render(request, 'index.html', {'result': result})