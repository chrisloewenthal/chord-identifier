#Some imporrtant libraries I can use
#PyAudio
#sounddevicee

#pitch dection
#librosa
#aubio
#crepe

#chord identification/music theory
#music 21
#mingus
#chordino




import wave
import time
import sys
import pyaudio
import numpy as np

CHUNK = 2**5
RATE = 44100
LEN = 5

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
player = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True, frames_per_buffer=CHUNK)


for i in range(int(LEN*RATE/CHUNK)): #go for a LEN seconds
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    player.write(data,CHUNK)


stream.stop_stream()
stream.close()
p.terminate()