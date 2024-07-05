from scamp import *
import melody_gen_v3
import time
import random
from trichord_alteration import scramble_trichords
from melody_gen_v3 import make_melody
from melody_gen_v3 import make_chord

   
while True: 
    s = Session(tempo=random.randint(60, 120))
    
    mel = s.new_part("piano")
    accomp = s.new_part("piano")
    
    s.start_transcribing()

    melody = make_melody()
    harmony = make_chord()
    
    print(make_melody())
    print(make_chord())

    
    def chords():
        for pitches, duration in harmony:
            accomp.play_chord(pitches, 0.55, duration)

            
    def notes():
        for pitch, duration in melody:
            mel.play_note(pitch, 0.7, duration)
            
    fork(chords)
    notes()

    performance = s.stop_transcribing()
    performance.to_score(title="RTMP 0.3", composer = "Generated with Real Time Midi Program 0.3 written by Gabriel Sagan").show_xml()

    sleep_time = random.uniform(4,10)
    
    time.sleep(sleep_time)
    
        
    
    

