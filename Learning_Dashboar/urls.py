"""Learning_Dashboar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from Dashboar import views as dash_views
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500, handler403, handler400


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Dashboar.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('register/', dash_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),
]

handler404 = 'Dashboar.views.error_404'
handler403 = 'Dashboar.views.error_403'
handler400 = 'Dashboar.views.error_400'
handler500 = 'Dashboar.views.error_500'
