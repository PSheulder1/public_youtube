from django.shortcuts import render, redirect, get_object_or_404

from authentification_app.models import Profile
from .models import YoutubeChannel, Video
# Create your views here.


def home(request):
    try:
        profile = Profile.objects.get(user=request.user)
        channel = YoutubeChannel.objects.filter(user=request.user)
    except Exception as e:
        profile = None
        channel=None

    allvideos = Video.objects.all()
    context = {
       'profile':profile,
       'channel' :channel,
       'allvideos':allvideos
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

    video = Video.objects.filter(user=request.user, channel=channel)

    context = {
       'channel' :channel,
       'videos':video,
    }

    return render(request, 'chaine_details.html', context)


def upload(request, pk):
    channel = get_object_or_404(YoutubeChannel, pk=pk)

    if request.method=="POST":
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        video = request.FILES.get('video')

        user = request.user

        Video.objects.create(titre=titre,
                              description=description,
                              video=video, user=user,
                                channel=channel)
        

        return redirect(f"/chaine/details/{pk}")
    
    return render(request, 'upload.html')



def banner(request, pk):
    channel = get_object_or_404(YoutubeChannel, pk=pk)
    if request.method=="POST":
        image = request.FILES.get('banner')
        channel.banner=image
        channel.save()

        return redirect(f"/chaine/details/{pk}")
    
    return render(request, 'banner.html')



def studio(request,pk):
    channel = get_object_or_404(YoutubeChannel, pk=pk)

    videos = Video.objects.filter(channel=channel, user=request.user)

    context = {
        'channel':channel,
        'videos':videos,
    }
    return render(request, 'studio.html', context)



def update(request, pk, channel_id):
    video = get_object_or_404(Video, pk=pk)
    if request.method =="POST":
        video.titre = request.POST.get('titre')
        video.description = request.POST.get('description')

        video_data = request.FILES.get('video')

        if video_data:
            video.video = video_data

        video.save()
        return redirect(f"/youtube-studio/{channel_id}")
    return render(request, 'update.html', {'video':video})



def delete(request, pk, channel_id):
    video = get_object_or_404(Video, pk=pk)
    if request.method=="POST":
        video.delete()
        return redirect(f"/youtube-studio/{channel_id}")

    context = {
        'video':video,
        'channel_id':channel_id,
    }
    return render(request, 'delete.html', context)
