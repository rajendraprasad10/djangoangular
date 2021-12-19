from django.contrib import admin
from django.conf.urls import url
from .views import department, employee, savefile
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^department/$', department, name="department"),
    url(r'^department/([0-9]+)$', department, name="department"),
    url(r'^employee/$', employee, name="employee"),
    url(r'^employee/([0-9]+)$', employee, name="employee"),
    url(r'^savefile/$', savefile, name="savefile"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
