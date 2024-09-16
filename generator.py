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
    
    #Use instead if wanting to external plugin
    #Windows: p = s.new_midi_part("piano", midi_output_device="loopMIDI Port")
    #Mac: p = s.new_midi_part("piano", "IAC")
    #Linux: p = s.new_midi_part("piano", midi_output_device="Midi Through Port 0")
    
    p = s.new_part("piano")
    
    #s.start_transcribing()

    melody = make_melody()
    
    print(s)
    print(melody)
    
    if melody:
        for note, duration in melody:
            p.play_note(note, 0.7, duration)
    
    #performance = s.stop_transcribing()
    #performance.to_score(title="RTMP", composer = "Generated with Real Time Midi Program written by Gabriel Sagan").show_xml()


    wait(random.randint(2, 7))