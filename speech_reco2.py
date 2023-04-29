from speech_recognition import Recognizer, Microphone
recognizer = Recognizer()
# On enregistre le son
with Microphone() as source:
    print("Réglage du bruit ambiant... Patientez...")
    recognizer.adjust_for_ambient_noise(source)
    print("Vous pouvez parler...")
    recorded_audio = recognizer.listen(source)
    print("Enregistrement terminé !")
    # with open('record.wav' , 'wb') as f:   ---------------------------------saving the file in wav format
    #    f.write( audio.get_wav_data() )
# Reconnaissance de l'audio
try:
    print("Reconnaissance du texte...")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="fr-FR"
        )
    print("Vous avez dit : {}".format(text))
except Exception as ex:
    print(ex)
    
    
