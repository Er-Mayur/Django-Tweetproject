from django.shortcuts import render,redirect, get_object_or_404
from tweet.models import Tweet
from tweet.forms import Tweet_form, UserRegistration_form

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index_view(request):
    return render(request , 'tweet/index.html')
 
def tweet_list(request):
    tweet = Tweet.objects.all().order_by('-created_at')
    d = {'tweet':tweet}
    return render(request , 'tweet/tweet_list.html', d)

@login_required
def tweet_create(request):
    
    if (request.method == 'POST'):
        tweet_form = Tweet_form(request.POST, request.FILES)
        if tweet_form.is_valid():
            tweet = tweet_form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        tweet_form = Tweet_form()    
        f = {'form': tweet_form}
    return render(request, 'tweet/tweet_from.html', f)    

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if (request.method == 'POST'):
        tweet_form = Tweet_form(request.POST, request.FILES, instance=tweet)
        if tweet_form.is_valid():
            tweet = tweet_form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
        else:
            f = {'form': tweet_form}
        
    else:
        tweet_form = Tweet_form(instance=tweet)
        f = {'form': tweet_form}
    return render(request, 'tweet/tweet_from.html', f)  

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST': 
        tweet.delete()         
        return redirect('tweet_list')
    d = {'tweet': tweet}
    return render(request, 'tweet/tweet_confirm_delete.html', d)

def register(request):
    registration_form = UserRegistration_form()
    f = {'form':registration_form}
    if request.method == 'POST':
        registration_form = UserRegistration_form(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=True)
            login(request, user)
            return redirect('tweet_list')
        
    return render(request, 'registration/registration.html', f)
