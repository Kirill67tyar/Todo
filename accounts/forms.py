from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    # функции в формах, начинающиеся с clean_ - создает в словаре cleaned_data пару key:value
    # К примеру def clean_something создает cleaned_data['something'] = результат метода (return)
    # но происхлдит это после валидации и функция cleaned_data - обозначают правила
    # по которым поле попадет в словарь после валидации
    # Почему после валидации? Потому что только после валидации у формы появится словарь cleaned_data


    def clean_password2(self):
        cd = self.cleaned_data  # Задать вопрос в слаке, почему self а не request
        # потому что мы здесь работаем не с конкретным запросом, а с объектом экземпляра класса
        # RegisterForm. По сути в качестве self здесь и выступает наш request (если точнее request,
        # который мы помещаем в форму)
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthdate', 'avatar')























































