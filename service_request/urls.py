from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [
    path('service_request/',views.make_service_request,name='service_request')
]
