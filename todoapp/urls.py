"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from tasks import views

urlpatterns = [
    path('sentry-debug/', views.trigger_error),
    path('admin-secure/', admin.site.urls),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('accounts/', include('accounts.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


# [Поэксперементировать со связями (request.user, 4 урок itvdn)]


# !!!Задать вопрос в слаке, от куда взялся profile в request.user.profile (см. 12.2.4 и вьюшку edit в accounts)!!!

# !!!!!1! id  Admin_077 = 4 Помни это когда делаешь миграции и привязываешь что-либо к админу!!!!



# Хвосты:
# 11.5.1(задание), 13.2.8 - не понял
# !!! Не настроено изменение паролей с помощью почты, и вообще отправка на почту. Натроить (см. 12.2.6 и слак)
# таки разместить сайт на хероку


# 19.3.3 skillfactory (и вообще весь 19 модуль) - про то, как выложить приложение в яндекс облако.
# но для этого нужен нормальный репазиторий на git-hub