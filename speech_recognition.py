import speech_recognition as sr
import wave
import pyaudio
r = sr.Recognizer()
sr.Microphone.list_microphone_names()
micro = sr.Microphone(device_index=5)
with micro as source:
    print("Speak!")
    audio_data = r.listen(source)
    print("End!")
result = r.recognize_google(audio_data)
print (">", result)
----------------------------------------------------------------------------------------------
#Recording from micro
import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 10
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Start Recording ...')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('... Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

#Getting the analyzed results with Google Speech recognition
import speech_recognition as sr
r = sr.Recognizer()

with sr.AudioFile(filename) as source:

    audio = r.record(source)
    try:
        # data = r.recognize_google(audio)
        data = r.recognize_google(audio, language="fr-FR")
        print(data)
    except:
        print("Please try again")

