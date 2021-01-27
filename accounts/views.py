from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View
from . import forms
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, ProfileEditForm
from .models import Profile
from . import models

from . import forms


class LoginView(View):
    def post(self, request, *args, **kwargs):
        form  = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            # если authenticate() выдает None - логина и/или пароля нет в базе
            # authenticate - возвращает объект пользователя по введенному логину и паролю

            if user is None:
                return HttpResponse('Неправильный логин и/или пароль')

            if not user.is_active:
                return HttpResponse('Ваш аккаунт заблокирован')

            # login - авторизует пользователя, полученного на предыдущем этапе
            login(request, user) # скорее всего запоминает, что сейчас пользователь залогинен.
                                 # возможно что с помощью функции login() заносится в настройки пользователя на сайте, куки
            # from itvdn:
            # login - функция, которая устанавливает сессионный ключ для нашего клиента
            # по ключу django определяет, выполнил ли user вход или нет
            # функция же logout() - этот ключ стирает, и все данны, которые сохранены были в юзере они исчезнут
            # произойдет разлогирование
            # в logout() мы добавляем request в качестве аргумента
            return HttpResponse('Добро пожаловать! Успешный вход')

        return render(request, 'accounts/login.html', {'form': form})


    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            # нельзя в django просто так присвоить user.password = form.cleaned_data['password']
            # джанго не хранит пароли в чистом виде
            # метод set_password() шифрует пароль
            # и сохраняет его в базу для пользователя, когда мы вызовем new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'accounts/registration_complete.html', {'new_user': new_user})
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': form})


@login_required
def edit(request):
    context = {}

    if request.method == 'POST':

        # просто помни, что переменные (как правило содержат в названии form) где в какую-то форму,
        # как ниже user_form и profile_form
        # мы передаем в аргументы request.POST - это по сути теги html.
        # django сам генерирует их в теги еще даже до того, как мы передаем их в контекст в render()
        # (кстати, не факт, что до того)
        # тем не менее формы выполняются лениво
        # (см. на значения user_form и profile_form в консоли)
        # а request.POST - это специальный тип данных, похожий на словарь - QueryDict
        # где:
        # key - один из параметров в пост запросе, как правило поле в бд, но может быть и имя поля
        # value - данные, которые мы передаем с запросом пост

        user_form = UserEditForm(instance=request.user, data=request.POST)

        # в аргумент instance мы добавляем т.к. редактируем мы только уже под определенным юзером
        # и чтобы не было ошибок валидации

        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        # а вот от-куда в request.user взялся profile, я не знаю
        # ЗАДАТЬ ВОПРОС В СЛАКЕ
        # теперь знаю, это связка таблиц one to one field
        # таким образом мы через одну таблицу обращаемся к другой

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context['user_form'] = user_form
    context['profile_form'] = profile_form
    print(f'request.POST - {request.POST} \nuser_form - {user_form} \nprofile_form - {profile_form} \n'
          f'request.user.profile - {request.user.profile} \nrequest.FILES - {request.FILES}')
    return render(request, 'accounts/edit.html', context)
# Create your views here.
