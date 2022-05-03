from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# from matplotlib.style import context
from core.models import Contact, Destination, Slider, State,News,RegionDataset,SubscribedUsers
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
import json
from core.forms import SignUpForm,LoginForm

# Create your views here.
from django.db.models import Avg, Sum

def index(request):
    state = ['ANDAMAN & NICOBAR ISLANDS',
             'ARUNACHAL PRADESH',
             'ASSAM & MEGHALAYA',
             'NAGA MANI MIZO TRIPURA',
             'SUB HIMALAYAN WEST BENGAL & SIKKIM',
             'GANGETIC WEST BENGAL',
             'ORISSA',
             'JHARKHAND',
             'BIHAR',
             'EAST UTTAR PRADESH',
             'WEST UTTAR PRADESH',
             'UTTARAKHAND',
             'HARYANA DELHI & CHANDIGARH',
             'PUNJAB',
             'HIMACHAL PRADESH',
             'JAMMU & KASHMIR',
             'WEST RAJASTHAN',
             'EAST RAJASTHAN',
             'WEST MADHYA PRADESH',
             'EAST MADHYA PRADESH',
             'GUJARAT REGION',
             'SAURASHTRA & KUTCH',
             'KONKAN & GOA',
             'MADHYA MAHARASHTRA',
             'MATATHWADA',
             'VIDARBHA',
             'CHHATTISGARH',
             'COASTAL ANDHRA PRADESH',
             'TELANGANA',
             'RAYALSEEMA',
             'TAMIL NADU',
             'COASTAL KARNATAKA',
             'NORTH INTERIOR KARNATAKA',
             'SOUTH INTERIOR KARNATAKA',
             'KERALA',
             'LAKSHADWEEP']

    dests = []
    for i in range(len(state)):
        dests.append(Destination())
        dests[i].name = state[i]
        dests[i].desc = "The City That Never Sleeps"
        dests[i].img = "destination_9.jpg"
        dests[i].price = 700

    st = State.objects.all().order_by('id')
    x=0
    state_l=[]
    for i in range(12):
        m=[]
        for j in range(3):
            m.append(st[x])
            x+=1
        state_l.append(m)
    

    # paginations

    paginator = Paginator(st, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    l = []
    for state in st:
        l.append(state.name)
    

    sl = Slider.objects.all()
    
    nw=News.objects.all()

    overall_annual_rainfall = RegionDataset.objects.values('YEAR').annotate(average_rainfall=Avg('ANNUAL'))
    
    monthly_overall_rainfall = RegionDataset.objects.values('YEAR').annotate(JAN=Sum('JAN'),FEB=Sum('FEB'),MAR=Sum('MAR'),APR=Sum('APR'),MAY=Sum('MAY'),JUN=Sum('JUN'),JUL=Sum('JUL'),AUG=Sum('AUG'),SEP=Sum('SEP'),OCT=Sum('OCT'),NOV=Sum('NOV'),DEC=Sum('DEC'))
    total_monthly_rainfall = {"Jan":0,"Feb":0,"Mar":0,"Apr":0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0,"Dec":0}    

    for item in monthly_overall_rainfall:
        total_monthly_rainfall["Jan"] +=item["JAN"]
        total_monthly_rainfall["Feb"] +=item["FEB"]
        total_monthly_rainfall["Mar"] +=item["MAR"]
        total_monthly_rainfall["Apr"] +=item["APR"]
        total_monthly_rainfall["May"] +=item["MAY"]
        total_monthly_rainfall["Jun"] +=item["JUN"]
        total_monthly_rainfall["Jul"] +=item["JUL"]
        total_monthly_rainfall["Aug"] +=item["AUG"]
        total_monthly_rainfall["Sep"] +=item["SEP"]
        total_monthly_rainfall["Oct"] +=item["OCT"]
        total_monthly_rainfall["Nov"] +=item["NOV"]
        total_monthly_rainfall["Dec"] +=item["DEC"]
    monthly_rain = []
    for item in total_monthly_rainfall.values():
        monthly_rain.append(item/114)

    overall_annual_rainfall_data = {}
    for item in overall_annual_rainfall:
        overall_annual_rainfall_data[item["YEAR"]] = item["average_rainfall"]
        
    context = {
        'home': "active",
        'dests': dests,
        'states': st,
        'state_l': state_l,
        'state':st,
        'slider': sl,
        "news":nw,
        "page_obj": page_obj,
        "welcome":"Rainfall Home Page",
        "line_chart": overall_annual_rainfall_data,
        "bar_chart": monthly_rain
    }
    return render(request, "index.html", context)


def contact(request):
    if request.method=="POST":
        namec=request.POST.get("names")
        emailc=request.POST.get("email")
        subjectc=request.POST.get("subject")
        messagec=request.POST.get("message")        
        data=Contact(name=namec,email=emailc,subject=subjectc,message=messagec)
        data.save()
        return redirect('/')
    
    c=Contact.objects.all()
    context={
        'contact': "active",
        'welcome':"Contact Page"
    }
    
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html', {'about': "active",'welcome':"About Us Page"})


def get_email(request):
    SubscribedUsers.objects.all().delete()
    if request.method == 'POST':
        stud_name=request.POST["name"]
        stud_email=request.POST["email"]
        subscribedUsers = SubscribedUsers(name=stud_name, email=stud_email)
        subscribedUsers.save()
        # send a confirmation mail
        subject = 'Regin Wise Rainfall Prediction'
        message = f"Hello {stud_name} , Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [stud_email, ]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/')
    return render(request, 'index.html')

def create_account(request):
    if request.method=="POST":
        form=SignUpForm(request.POST,label_suffix=" ")
        if form.is_valid():
            messages.success(request,"Congratulation Your ID has been created !!")
            user=form.save()
            return redirect("/login/")
    else:
        form=SignUpForm(label_suffix=" ")
        
    context={
        'signup_form':form,
        "welcome":"To Sign Up Page",
        "signup":"active"
    }
    return render (request,'signup.html',context)
       

# Login
def user_login(request):
    # if not request.user.is_authenticated :: means user is not logged in so the else part will be executed
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfuly")
                    return redirect("/")
                else:
                    messages.info(request,"invalid credentials")
                    return redirect("login/")
        else:
            form = LoginForm()
        context = {
            'login_form': form,
            "welcome":"To Login Page",
            "login":"active"
        }
        return render(request, 'login.html', context)
    else:
        # this will execute when the user is already logged in
        return redirect('/')
    
def user_logout(request):
    logout(request)
    messages.info(request,"You have logged out successfully !!")
    return redirect("/")