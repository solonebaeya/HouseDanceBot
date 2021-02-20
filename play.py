#coding=utf-8
import pyaudio
import wave
from tqdm import tqdm
import time
import random
import os

def file_name(file_dir):
    for files in os.walk(file_dir):
        wavefile = files[2]
        return wavefile

def play_audio(nunu):
        CHUNK = 1024

        wf = wave.open('BasicSteps/'+nunu, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

        data = wf.readframes(CHUNK)

        datas = []
        while len(data) > 0:
            data = wf.readframes(CHUNK)
            datas.append(data)

        for d in tqdm(datas):
            stream.write(d)

        time.sleep(15)

        stream.stop_stream()
        stream.close()

        p.terminate()

def main():
    hel = file_name('BasicSteps')
    while(1):
        a = random.randint(0,25)
        nunu = hel[a]
        play_audio(nunu)

if __name__ == '__main__':
    main()


