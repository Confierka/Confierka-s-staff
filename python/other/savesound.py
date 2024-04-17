from scipy.io import wavfile
import numpy as np
from math import *



def sound_sin(freq,t):
    koeffs = [20,8,4,2,1]
    sm =sum(koeffs)
    res = 0
    for i in range(len(koeffs)):
        res += koeffs[i]*sin(2*pi*freq*t*(i+1))/sm
    return res
def sound_square(freq,t):
    dt = 1/freq
    x = t - floor(t/dt)*dt
    if x> dt/2:
        return -1
    return 1
def sound_saw(freq,t):
    dt=1/freq
    return 2*(t-floor(t/dt)*dt)*freq-1

def sound(freq,t,instr = 0):
    if instr==0:
        return sound_sin(freq,t)
    if instr==1:
        return sound_square(freq,t)
    if instr==2:
        return sound_saw(freq,t)
    

def play_note(dur,num,loudness = 1,instr=0):
   


    t_array = [1/rate*i for i in range(int(rate*dur))]

    if num is None: 
        a_array = [0 for t in t_array]
    else: 
        freq = 220 * (2**(1/12*num))
        a_array = [int(loudness*10000*sound(freq,t,instr)) for t in t_array]


    return a_array

def play_track(notes,instr=0):
    result = []

    for dur, note,loudness in notes:
        result+= play_note(dur,note,loudness,instr)
    return np.array(result)


rate = 24000

notes= [
    [0.25,0,1],
    [0.25,1,1],
    [0.25,0,1],
    [0.25,None,1],
    [0.25,0,1],
    [0.25,1,1],
    [0.25,0,1],
    [0.25,1,1],
    [0.25,4,1],
    [0.25,5,1],
    [0.25,4,1],
    [0.25,None,1],
    [0.25,4,1],
    [0.25,5,1],
    [0.5,0,1],


]

track=play_track(notes)

notes2=[
    [0.5,0,0.5],
    [0.5,None,0.5],
    
    [0.5,3,0.5],
    [0.5,None,0.5],

    [0.5,0,0.5],
    [0.5,None,0.5],

    [0.5,4,0.5],
    [0.5,None,0.5],


]
track2=play_track(notes2,1)

notes3= [
    [1,-12,1],
    [1,-9,1],
    [1,-12,1],
    [1,-8,1]
]

track3 =play_track(notes3,2)
wavfile.write('test.wav',rate,np.array((track+track2+track3)/3,dtype=np.int16))
