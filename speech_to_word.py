import sys
import speech_recognition as sr

r = sr.Recognizer()
file_name = sys.argv[1] + ".wav"

with sr.Microphone() as source:
    print ("Please TSpeak")
    try:
        audio = r.record(source, duration=5)
        with open(file_name, "wb") as f:
            f.write(audio.get_wav_data())
	
        get_file = sr.AudioFile(file_name)
        with get_file as source:
            audio = r.record(source)

        text = r.recognize_google(audio)
    except:
        text = "Unable to recognize speech"
    print(text)
