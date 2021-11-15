import os
import pandas as pd
from pytube import YouTube
from moviepy.editor import *
import librosa
import numpy as np
import shutil  #업로드 된 동영상 사본 만들기 위해 필요
from td_utils import *

DATA_BASE_PATH = "F:\pro\\aistory\\pblcodes\\data\\"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main(video, idd=0):
    data_output_folder = DATA_BASE_PATH + "\\" + str(idd)+ "\\"
    print(bcolors.OKGREEN + '\nplease wait! \n' + bcolors.ENDC)
    shutil.copyfile(DATA_BASE_PATH+video, data_output_folder+"copied_"+video)   #사본
    videoclip = VideoFileClip(data_output_folder+"copied_"+video)
    audioclip = videoclip.audio
    audioclip.write_audiofile(data_output_folder+"tmp.wav")
    y = [0,1,1,0,0,0,1,0,1,1] #26초에 0.5 묵음
    make_quiet_wav(data_output_folder+"tmp.wav", y, data_output_folder+"{}_result_{}.wav".format(idd, video))
    videoclip = videoclip.set_audio(AudioFileClip(data_output_folder+"{}_result_{}.wav".format(idd, video)))
    videoclip = videoclip.subclip(28, 34)
    videoclip.write_videofile(data_output_folder+"{}_result_{}.mp4".format(idd, video))
    videoclip.write_videofile(data_output_folder+"{}_origin_{}.mp4".format(idd, video))

    print(bcolors.OKGREEN + '\nNow you can check!!! ' + bcolors.ENDC)

if __name__ == '__main__':
    video= "testVideo.mp4"
    idd = int(input('ID: '))
    data_output_folder = DATA_BASE_PATH + "\\" + str(idd)
    try:
        if not os.path.exists(data_output_folder):
            os.makedirs(data_output_folder)
    except OSError:
        print('Error: Creating directory. ' + data_output_folder)
        quit()
    main(video, idd)