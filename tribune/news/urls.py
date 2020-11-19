from django.urls import include, path

# from django_registration.backends.one_step.views import RegistrationView


from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('today', views.news_today, name='news_today'),
    path('tinymce/', include('tinymce.urls')),
    # path(
    #     'accounts/register/',
    #     RegistrationView.as_view(success_url='/profile/')
    # ),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
