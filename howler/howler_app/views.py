from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from howler_app.forms import SignUpForm


@login_required(login_url="login/")
def all_howls(request):
    howlobj = Howler.objects.all().order_by('-creation_date')
    alluserprofiles = UserProfile.objects.all()
    return render(request,'howler_app/all_howls.html',{'howlobj':howlobj,'alluserprofiles':alluserprofiles})

            
@login_required(login_url="login/")
def add_follower(request):
    if request.method == 'POST':
        form = AddFollowerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            add_user = User.objects.filter(username = name)
            current_user = UserProfile.objects.filter(user=request.user)
            follow_user = UserProfile.objects.filter(user=add_user)

            for y in follow_user:
                for x in current_user:
                    x.follows.add(y)
            return redirect('/homepage/')
    else:
        form = AddFollowerForm()

    return render(request, 'howler_app/add_follower.html',{'form':form,})

@login_required(login_url="login/")
def homepage(request):
    current_user = UserProfile.objects.filter(user=request.user)
    following = current_user[0].follows.all()
    templist = []


    for p in following:
        templist.append(Howler.objects.filter(user = p.user))
    list_of_howls = []
    for howlset in templist:
        for p in howlset:
            list_of_howls.append(p)

    #sort list acc to time
    list_of_howls.sort(key = lambda r: r.creation_date)
    list_of_howls.reverse()
    context_dict = { 'list_of_howls':list_of_howls, 'following':following}



    return render(request,"howler_app/homepage.html",context=context_dict)



@login_required(login_url="login/")
def all_users(request):
    users = UserProfile.objects.all()
    return render(request,'howler_app/all_users.html',{'users':users,})

@login_required(login_url="login/")
def view_user(request,user_id):
    users = UserProfile.objects.filter(pk = user_id)
    allhowls = Howler.objects.filter(user = users[0].user).order_by('-creation_date')
    return render(request,'howler_app/view_user.html',{'user_id':user_id,'users':users,'allhowls':allhowls})
    


@login_required(login_url="login/")
def add_howl(request):
    form = HowlerForm()

    if(request.method=='POST'):
        form = HowlerForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect('/profile/')

    else:
        print(form.errors)

    return render(request,'howler_app/add_howl.html', {'form':form})


@login_required(login_url="login/")
def user_profile(request):
    current_user = UserProfile.objects.filter(user=request.user)
    user_howls = Howler.objects.filter(user=request.user).order_by('-creation_date')

    context_dict={'current_user':current_user,'user_howls':user_howls}
    return render(request,'howler_app/user_profile.html',context=context_dict)

@login_required(login_url="login/")
def my_followers(request):
    current_user = UserProfile.objects.filter(user=request.user)
    following = current_user[0].follows.all()
    return render(request, 'howler_app/my_followers.html',{'following':following})


def set_defaults(request):
    users = User.objects.all()
    list_of_users = []
    for x in users:
        list_of_users.append(x)

    recently_added_user=list_of_users[-1]
    UserProfile.objects.create(user = recently_added_user)



def index(request):
    return redirect('/login/')


def signup(request):
    form = SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            set_defaults(request)
            return redirect('/login/')
        else:
            print(form.errors)
    return render(request,'howler_app/signup_form.html',{'form':form})
@login_required(login_url="login/")
def search(request):
    if request.method == 'POST':
        srch=request.POST['srh']

        if srch:
            match = UserProfile.objects.filter(Q(user__username__iexact=srch))

            if match:
                return render(request,'howler_app/search.html', {'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'howler_app/search.html')
