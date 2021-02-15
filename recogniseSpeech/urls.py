from django.urls import include, path
from . import views

urlpatterns = [
    path('api/v1/speechtotext', views.ConvertSpeechToText.as_view())
]
