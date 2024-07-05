from scamp import *
import melodygen
import time
import random


while (True):
    
    s = Session(tempo=100)
    clar=s.new_part("Synth Bass")
    s.start_transcribing()

    melody = melodygen.make_melody()

    for pitch, duration in melody:
        clar.play_note(pitch, 0.7, duration)
        
    
    sleep_time = random.uniform(4,10)
    
    time.sleep(sleep_time)

