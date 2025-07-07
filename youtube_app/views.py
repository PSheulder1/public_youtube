from django.shortcuts import render, redirect, get_object_or_404

from authentification_app.models import Profile
from .models import YoutubeChannel
# Create your views here.


def home(request):
    try:
        profile = Profile.objects.get(user=request.user)
        channel = YoutubeChannel.objects.filter(user=request.user)
    except Exception as e:
        profile = None
        channel=None

    context = {
       'profile':profile,
       'channel' :channel
    }
    return render(request, 'index.html', context)

def channel(request):
    if request.method=="POST":
        name = request.POST.get('channel_name')
        description = request.POST.get('description')
        image = request.FILES.get('image',None)

        data = YoutubeChannel.objects.create(user=request.user,name=name,
                                              description=description, image=image)
        data.save()
        return redirect('home')


    return render(request, 'channel.html')


def chaine_details(request, pk):
    channel = get_object_or_404(YoutubeChannel, pk=pk)

    return render(request, 'chaine_details.html', {'channel':channel})
