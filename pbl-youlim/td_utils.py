import os

from pydub import AudioSegment
import librosa
import numpy as np
import soundfile as sf
DATA_BASE_PATH = "F:\pro\\aistory\\pblcodes\\data\\"
def make_quiet_wav(wav, y, output_name):
    quiet, _ = librosa.load(DATA_BASE_PATH+'quiet.wav', sr=44100)
    data, _ = librosa.load(wav, sr=44100)
    length = len(y)
    for i in range(0, length):
        tmp = int(len(data)*(i)/length)
        t_1 = y[i-1]
        t = y[i]
        if (t_1 == 0) and (t == 1):
            if tmp > 22000:
                data[tmp-22000:tmp] = quiet[:22000]*1.0
            else:
                data[:tmp] = quiet[:tmp]*1.0
    sf.write(output_name, data, 44100)

# def output_postprocessing(outputs, th):
#     for output in outputs:
#         output[output<th] = 0
#         output[output>=th] = 1
#     return outputs