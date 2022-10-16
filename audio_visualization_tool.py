import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import TclError

CHUNK: int = 1024 * 2           # sample per frame
FORMAT: int = pyaudio.paInt16
CHANNELS: int = 1               # singe channel for microphone
RATE: int = 44100               # samples oer second

figure, axes = plt.subplot(1, figsize=(15, 7))

pya = pyaudio.PyAudio()

# get list of available inputs
info = pya.get_host_api_info_by_index(0)
num_devices = info.get('deviceCount')

for i in range(0, num_devices):
    if(pya.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id", i, " - ", pya.get_device_info_by_host_api_device_index(0, 1).get('name'))

audio_input = input("\n\nSelect input by Device id: ")

while not audio_input.isdigit():
    print("You didn't enter a number.")
    audio_input = input("\n\nSelect input by Device id: ")

# stream object to get data from microphone
stream = pya.open(
    input_device_index=int(audio_input),
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK,
)

# variable for plotting
x = np.arange(0, 2 * CHUNK, 2)

# create a line object with random data
line, = axes.plot(x, np.random.rand(CHUNK), '-', lw=2)

# basic formatting for the axes
axes.set_title('AUDIO WAVEFORM')
axes.set_xlabel('sample')
axes.set_ylabel('volume')
axes.set_ylim(0, 255)
axes.set_xlim(0, 2 * CHUNK)
plt.setp(axes, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

plt.show(block=False)

print('stream started')

# for measuring frame rate
frame_count: int = 0
start_time: float = time.time()

while True:
    # binary data
    data = stream.read(CHUNK)

    # convert data to integers, make np array, then offset it by 127
    data_int: tuple = struct.unpack(str(2 * CHUNK) + 'B', data)

    # create np array and offset by 128
    data_np = np.array(data_int, dtype='b')[::2] + 128

    line.set_ydata(data_np)
















