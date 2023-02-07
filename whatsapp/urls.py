from django.urls import path
from . import views

urlpatterns = [
    path('send-message/', views.SendMessageAPI.as_view(), name='send-message'),
    path('download-template/', views.ContactsTemplateDownload.as_view(), name='download-template'),
]