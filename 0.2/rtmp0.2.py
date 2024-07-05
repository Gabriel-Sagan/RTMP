from scamp import *
import melody_gen_v2
import time
import random


while True:
    
    s = Session(tempo=random.randint(60, 120))
    
    clar = s.new_midi_part("piano", midi_output_device="loopMIDI Port")
    
    s.start_transcribing()

    melody = melody_gen_v2.make_melody()
    
    for pitch, duration in melody:
        clar.play_note(pitch, 0.7, duration)
    
    performance = s.stop_transcribing()
    performance.to_score(title="RTMP 0.2", composer = "Generated with Real Time Midi Program 0.2 written by Gabriel Sagan").show_xml()
        
    
    sleep_time = random.uniform(4,10)
    
    time.sleep(sleep_time)
    
