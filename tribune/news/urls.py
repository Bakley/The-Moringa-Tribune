from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('today', views.news_today, name='news_today'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
