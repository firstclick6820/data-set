from django.shortcuts import render


# import models
from .models import AffiliatePrograms





def HomePage(request):
    records =  AffiliatePrograms.objects.all().order_by('-created_at')

    context = {
        'records': records
    }
    return render(request, 'core/home.html', context)