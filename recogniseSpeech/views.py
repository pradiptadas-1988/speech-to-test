import os
from django.shortcuts import render
from rest_framework.views import APIView
import speech_recognition as sr
from rest_framework.response import Response
from recogniseSpeech.serializers import GetAudioSerializer

# Create your views here.
path = "/home/audio_files"

class ConvertSpeechToText(APIView):
    serializer_class = GetAudioSerializer
    def get(self, request):
        """
        Get the requested audio file from the path and convert to speech

        """
        #import pdb
        #pdb.set_trace()
        #r = sr.Recognizer()
        #path_audio = path + '/st_file.wav'
        #audio_file_path = sr.AudioFile(path_audio)
        #with audio_file_path as source:
        #    audio = r.record(source)
        #try:
        #    text = r.recognize_google(audio)
        #except:
        #    text = "Unable to recognize speech"
        return Response({"text": ""})

    def post(self, request):
        """
        get the required .wav file and save it in the path
        """
        
        r = sr.Recognizer()
        audio_file_name = request.POST['audio_file_name']
        path_audio = path + '/' + audio_file_name
        audio_file_path = sr.AudioFile(path_audio)
        with audio_file_path as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = "Unable to recognize speech"
        return Response({"text": text})
       


