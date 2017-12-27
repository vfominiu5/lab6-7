from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django import forms
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import  *

# Create your views here.
class TravelerList(ListView):
    model = Traveler
    template_name = 'traveler_list.html'


class HotelList(ListView):
    model = Hotel
    template_name = 'hotel_list.html'


class BookingList(ListView):
    model = Booking
    template_name = 'booking_list.html'


def registration_dumb(request):
    errors = {}
    request.encoding = 'utf-8'
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['uname']='Введите логин'
        elif len(username) < 5:
            errors['uname']='Длина логина должна быть не меньше 5 символов'

        if User.objects.filter(username=username).exists():
            errors['uname']='Такой логин уже занят'

        password = request.POST.get('password')
        if not password:
            errors['psw']='Введите пароль'
        elif len(password) < 8:
            errors['psw']='Длина пароля должна быть не меньше 8 символов'

        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['psw2']='Пароли должны совпадать'

        email = request.POST.get('email')
        if not email:
            errors['email']='Введите email'

        last_name = request.POST.get('last_name')
        if not last_name:
            errors['lname']='Введите фамилию'

        first_name = request.POST.get('first_name')
        if not first_name:
            errors['fname']='Введите имя'

        if not errors:
            user = User.objects.create_user(username, email, password)
            trav = Traveler()
            trav.user = user
            trav.first_name = first_name
            trav.last_name = last_name
            trav.save()
            return HttpResponseRedirect('/labs/travelers')
        else:
            context = {'errors':errors, 'username':username, 'email': email, 'last_name': last_name, 'first_name': first_name}
            return render(request, 'registration_dumb.html',context)

    return render(request, 'registration_dumb.html',{'errors':errors})


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5,label='Логин')
    password = forms.CharField(min_length=8,widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите ввод')
    email = forms.EmailField(label='Email')
    last_name = forms.CharField(label='Фамилия')
    first_name = forms.CharField(label='Имя')


def registration_traveler(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        is_val = form.is_valid()
        data = form.cleaned_data
        if data['password']!=data['password2']:
            is_val = False
            form.add_error('password2',['Пароли должны совпадать'])
        if User.objects.filter(username=data['username']).exists():
            form.add_error('username',['Такой логин уже занят'])
            is_val = False

        if is_val:
            data = form.cleaned_data
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            trav = Traveler()
            trav.user = user
            trav.first_name = data['first_name']
            trav.last_name = data['last_name']
            trav.save()
            return HttpResponseRedirect('/labs/authorization')
    else:
        form = RegistrationForm()

    return render(request, 'registration_traveler.html',{'form':form})


@login_required(login_url='/labs/authorization')
def success_authorization(request):
    return HttpResponseRedirect('/labs')


def success_authorization_dumb(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/labs/')
    else:
        return HttpResponseRedirect('/labs/authorization')


def authorization(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['uname']='Введите логин'
        elif len(username) < 5:
            errors['uname']='Длина логина должна быть не меньше 5 символов'

        password = request.POST.get('password')
        if not password:
            errors['psw']='Введите пароль'
        elif len(password) < 8:
            errors['psw']='Длина пароля должна быть не меньше 8 символов'

        user = authenticate(request, username=username, password=password)
        if user is None and 'uname' not in errors.keys() and 'psw' not in errors.keys():
            errors['login'] = 'Логин или пароль введены неправильно'

        if not errors:
            login(request,user)
            #return HttpResponseRedirect('/labs/success_authorization_dumb')
            return HttpResponseRedirect('/labs/success_authorization')
        else:
            context = {'errors':errors}
            return render(request, 'authorization.html',context)

    return render(request, 'authorization.html',{'errors':errors})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/labs/')

class AutorizationForm(forms.Form):
    pass


def index(request):
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris venenatis sem eu neque elementum semper. Aenean a quam enim. Praesent dictum, magna non tincidunt luctus, tortor tellus lobortis lorem, eu sodales felis libero sit amet nulla. Nam rhoncus faucibus fermentum. Sed nec est tellus. Vestibulum vitae volutpat sem, et ullamcorper tortor. Donec venenatis libero vel metus luctus eleifend. Praesent eleifend metus tincidunt, tempus leo a, volutpat dui." \
            "Integer mattis cursus ante, non maximus ligula pellentesque eu. Phasellus semper libero ac tortor auctor placerat. Quisque quam ipsum, gravida vitae risus at, fringilla vestibulum nibh. Donec fermentum accumsan velit vel rutrum. In imperdiet, leo nec finibus vehicula, tellus massa vehicula arcu, non feugiat leo ex ac dolor. In sagittis augue quis metus suscipit dapibus. Curabitur ultrices erat malesuada, viverra arcu ornare, accumsan est." \
            "Suspendisse dignissim odio at nibh malesuada, sit amet volutpat ante pellentesque. Ut id lorem commodo, mollis sapien sit amet, vestibulum magna. Curabitur a convallis augue, eu hendrerit ipsum. Cras semper dolor id mauris porttitor, a sagittis felis mattis. In hac habitasse platea dictumst. Curabitur eu ex vel orci ultrices commodo. Integer ac ligula massa."

    news = [{'id':i} for i in range(10)]
    for n in news:
        id = n['id']
        n['title'] = 'Title #'+str(id+1)
        n['content'] = lorem[:150]+'...'

    context = {'news_list': news[:5]}
    return render(request,'index.html',context)


def single_news(request,id):
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris venenatis sem eu neque elementum semper. Aenean a quam enim. Praesent dictum, magna non tincidunt luctus, tortor tellus lobortis lorem, eu sodales felis libero sit amet nulla. Nam rhoncus faucibus fermentum. Sed nec est tellus. Vestibulum vitae volutpat sem, et ullamcorper tortor. Donec venenatis libero vel metus luctus eleifend. Praesent eleifend metus tincidunt, tempus leo a, volutpat dui." \
            "Integer mattis cursus ante, non maximus ligula pellentesque eu. Phasellus semper libero ac tortor auctor placerat. Quisque quam ipsum, gravida vitae risus at, fringilla vestibulum nibh. Donec fermentum accumsan velit vel rutrum. In imperdiet, leo nec finibus vehicula, tellus massa vehicula arcu, non feugiat leo ex ac dolor. In sagittis augue quis metus suscipit dapibus. Curabitur ultrices erat malesuada, viverra arcu ornare, accumsan est." \
            "Suspendisse dignissim odio at nibh malesuada, sit amet volutpat ante pellentesque. Ut id lorem commodo, mollis sapien sit amet, vestibulum magna. Curabitur a convallis augue, eu hendrerit ipsum. Cras semper dolor id mauris porttitor, a sagittis felis mattis. In hac habitasse platea dictumst. Curabitur eu ex vel orci ultrices commodo. Integer ac ligula massa."

    news = [{'id':i} for i in range(10)]
    for n in news:
        idx = n['id']
        n['title'] = 'Title #'+str(idx+1)
        n['content'] = lorem
    context = {'news': news[int(id)]}
    return render(request,'single_news.html',context)
