import sounddevice as sd
import numpy as np
import datetime

duration = 5 
sample_rate = 44100

print("Recording...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
sd.wait()

filename = f"recording_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav"
np.savetxt(filename, audio_data)

print(f"Recording saved as {filename}")