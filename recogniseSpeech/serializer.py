from rest_framework import serializers

class GetAudioSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   audio_file_name = serializers.StringField()
 


