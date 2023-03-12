#voice_recorder
import sounddevice
from scipy.io.wavfile import write
fs = 44100#rate
second = int(input("Duration:: "))
print("recording")
record_voice = sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
print("finished")