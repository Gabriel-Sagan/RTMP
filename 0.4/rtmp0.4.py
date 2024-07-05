from scamp import *
from melody import *
import time
import random

trichord_input()
duration_input()
temp = tempo_input()

while True:
    
    s = None
    
    if isinstance(temp, list):
        if len(temp) == 2: 
            temp_int = [int(num) for num in temp]
            s = Session (tempo = random.randint(min(temp_int), max(temp_int)))
    else:
        s = Session(tempo = int(temp))
    
    #Use instead if not utilizing external plugin
    #s.new_part("piano")
    p = s.new_midi_part("piano", midi_output_device="loopMIDI Port")
    
    
    s.start_transcribing()

    melody = make_melody()
    
    print(s)
    print(melody)
    
    if melody:
        for note, duration in melody:
            p.play_note(note, 0.7, duration)
    
#     performance = s.stop_transcribing()
#     performance.to_score(title="RTMP 0.4", composer = "Generated with Real Time Midi Program 0.4 written by Gabriel Sagan").show_xml()
        
    
    sleep_time = random.uniform(2, 5)
    
    time.sleep(sleep_time)

    