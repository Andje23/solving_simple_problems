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