from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import EmailMessage
# from django.core.mail import send mail, BadHeaderError
from .models import Usr_Profile, FirstLogin, MessMaharaj
from .models import Day
from chatmaster.p2p_chat import *

from home.forms import Usr


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def log_in(request):
    if request.method == "POST":
        # print "reqoest--",request.POST,"###"
        roll_no = request.POST['roll_no']
        pswd = request.POST['pswd']
        usr = authenticate(username=roll_no, password=pswd)

        if usr is not None:
            u = User.objects.get(username=roll_no)
            print "###", u.username, "###"
            NewUsr = Usr_Profile.objects.get(user=u)
            print "###", NewUsr
            login(request, usr)
            return render(request, 'profile.html', {'NewUsr': NewUsr})

            # return HttpResponse("<h1> Congrats! Successfully LoggedIn <br/></h1>")
        else:
            return HttpResponse("<h1>Unauthorised User... Register First...</h1>")
    else:
        return HttpResponse("<h1>Try Again</h1>")


def log_out(request):
    logout(request)
    return HttpResponse("<h1>Logout Successfully</h1>")


def register1(request):
    return render(request, 'register1.html')


def display_menu(request):
    context = {}
    mon = Day.objects.get(name="mon")
    context['mon'] = mon
    tue = Day.objects.get(name="tue")
    context['tue'] = tue
    wed = Day.objects.get(name="wed")
    context['wed'] = wed
    thu = Day.objects.get(name="thu")
    context['thu'] = thu
    fri = Day.objects.get(name="fri")
    context['fri'] = fri
    sat = Day.objects.get(name="sat")
    context['sat'] = sat
    sun = Day.objects.get(name="sun")
    context['sun'] = sun
    #context['mess'] = "D. G. Mess"
    return render(request, 'menu.html', context)


def createUsr1(request):
    error_msg = ""
    if request.method == "POST":
        if request.POST['user_password']:
            NewUsr = User(request.POST)
            if NewUsr:
                roll_no = request.POST['roll_no']
                # user_email1 = NewUsr.cleaned_data['user_email']
                user_password = request.POST['user_password']
                usr = User.objects.create_user(username=roll_no, password=user_password)
                usr.save()

                return render(request, 'register2.html', {})  # complete url
            else:
                print NewUsr.errors
                error_msg = "Please enter all data fields correctly! Thank you..."
                return render(request, 'register1.html', {"error_msg": error_msg})
        else:
            error_msg = "Your Password didn't match! Try again..."
            return render(request, 'register1.html', {"error_msg": error_msg})
    else:
        return HttpResponse('<h2> ForBidden </h2>')


def createUsr2(request):
    error_msg = ""
    if request.method == "POST":
        ur = request.POST['user']
        u = User.objects.get(username=ur)  # .get(roll_no=ur)
        un = request.POST['user_name']
        ue = request.POST['user_email']
        rn = request.POST['Room_number']
        pn = request.POST['Phone_number']
        um = request.POST['user_mess']
        hn = request.POST['hostel_name']
        # ub = request.POST['user_balance']
        # ue = request.POST['user_expense']
        Bn = request.POST['Branch_name']
        Y = request.POST['Year']
        NewUsr = Usr_Profile(user=u, user_name=un, user_email=ue, Room_number=rn, Phone_number=pn, user_mess=um,
                             hostel_name=hn, user_balance=12000, user_expense=0, Branch_name=Bn, Year=Y)
        subject_message = "Registration Successful"
        msg = " Congarts! You have been Successfully registered on the mess management website..."
        email = EmailMessage(subject_message, msg, 'sender smtp gmail' + 'itwpractice@gmail.com',
                             [ue], headers={'Reply-to': 'noreply@gmail.com'})
        email.send()

        if NewUsr:
            NewUsr.save()
            login(request, NewUsr.user)
            return render(request, 'profile.html', {'NewUsr': NewUsr})
        else:
            error_msg = "Please enter all data fields correctly! Thank you..."
            return render(request, 'register2.html', {'error_msg': error_msg})
    else:
        return redirect('/')


def edit_menu_dis(request):
    return render(request,'menu_edit.html')

def menu_edit(request):
    if request.method == "POST":
        mon = Day(name="mon", breakfast=request.POST['mon1'], lunch=request.POST['mon2'],
                  dinner=request.POST['mon3']).save()
        tue = Day(name="tue", breakfast=request.POST['tue1'], lunch=request.POST['tue2'],
                  dinner=request.POST['tue3']).save()
        wed = Day(name="wed", breakfast=request.POST['wed1'], lunch=request.POST['wed2'],
                  dinner=request.POST['wed3']).save()
        thu = Day(name="thu", breakfast=request.POST['thu1'], lunch=request.POST['thu2'],
                  dinner=request.POST['thu3']).save()
        fri = Day(name="fri", breakfast=request.POST['fri1'], lunch=request.POST['fri2'],
                  dinner=request.POST['fri3']).save()
        sat = Day(name="sat", breakfast=request.POST['sat1'], lunch=request.POST['sat2'],
                  dinner=request.POST['sat3']).save()
        sun = Day(name="sun", breakfast=request.POST['sun1'], lunch=request.POST['sun2'],
                  dinner=request.POST['sun3']).save()
        mess = "D. G. Mess"
        #context = {'mon': mon, 'tue': tue, 'wed': wed, 'thu': thu, 'fri': fri, 'sat': sat, 'sun': sun, 'mess': mess}
        return render(request, 'menu.html', {'mon': mon, 'tue': tue, 'wed': wed, 'thu': thu, 'fri': fri, 'sat': sat, 'sun': sun, 'mess': mess})


def maharajlogin(request):
    return render(request, 'maharaj_login.html')


def log_in_maharaj(request):
    if request.method:
        email = request.POST['user_email']
        pswd = request.POST['user_password']
        usr = authenticate(username=email, password=pswd)

        if usr is not None:
            u = User.objects.get(username=email)
            if len(FirstLogin.objects.all()) == 0:
                fst_lgin = FirstLogin(Maharaj=1)
                return redirect('/maharaj/comp_pro')
            NewUsrmaharaj = MessMaharaj.objects.get(user=u)
            # login(request,usr)
            return render(request, 'mess_maharaj.html', {'mm': NewUsrmaharaj})

            # return HttpResponse("<h1> Congrats! Successfully LoggedIn <br/></h1>")
        else:
            return HttpResponse("<h1>Unauthorised User... Register First...</h1>")
    else:
        return HttpResponse("<h1>Try Again</h1>")


def MMcompPro(request):
    return render(request, 'maharaj_register.html')


def save_credential(request):
    if request.method == "POST":
        u = User.objects.get(username=request.POST['user_id'])
        mm = MessMaharaj(user=u, maharaj_mob=request.POST['user_id'], maharaj_name=request.POST['user_name'],
                         maharaj_mess=request.POST['user_mess']).save()
        return render(request, 'mess_maharaj.html', {'mm': mm})
    else:
        return redirect('/maharaj/comp_pro/')


def chat(request):
    root = tk.Tk()
    p2p_chat = P2pChat(master = root)
    p2p_chat.mainloop()