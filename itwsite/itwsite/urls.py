"""itwsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage),
    url(r'^login/$', log_in),
    url(r'^signup/$', register1),
    #url(r'^registered$', createUsr1),
    url(r'^regstep1/', createUsr1),
    url(r'^regstep2/', createUsr2),
    url(r'^logout/',log_out),
    url(r'^menu/',display_menu),
    url(r'^edit_menu/',menu_edit),
    url(r'^set_menu/',edit_menu_dis),
    url(r'^chat/$', chat),
    url(r'^maharaj_login/',maharajlogin),
    url(r'^profile_maharaj/',log_in_maharaj),
    url(r'^maharaj/comp_pro/',MMcompPro),
    url(r'^register/success/',save_credential),


]
