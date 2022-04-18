
from django.conf.urls import url
from demoreact12  import views


urlpatterns = [
    url(r'^$',views.input),
    url(r'Sub',views.add)
]
