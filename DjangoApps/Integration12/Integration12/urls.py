
from django.contrib import admin
from django.urls import path
from demoreact12 import views
from django.conf.urls import url,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/',include('demoreact12.urls'))
    #url(r'^$',views.home)

]
