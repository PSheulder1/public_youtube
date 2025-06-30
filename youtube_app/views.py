from django.shortcuts import render

from authentification_app.models import Profile

# Create your views here.


def home(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Exception as e:
        profile = None
    return render(request, 'index.html', {'profile':profile})
