from scamp import *
import melody_gen_v4
import time
import random
from trichord_alteration import scramble_trichords
from melody_gen_v4 import make_melody
from melody_gen_v4 import make_chord

   
while True:
    
    s = Session(tempo=random.randint(60, 120))
    
    mel = s.new_midi_part("piano", midi_output_device="loopMIDI Port")
    accomp = s.new_midi_part("piano", midi_output_device="loopMIDI Port")
    
    s.start_transcribing()

    single_trichord = random.choice(scramble_trichords())

    melody, trichords = make_melody()
    harmony = make_chord(trichords)
    
    print(melody)
    print(harmony)

    
    def chords():
        for pitches, duration in harmony:
            accomp.play_chord(pitches, 0.55, duration)

            
    def notes():
        for pitch, duration in melody:
            mel.play_note(pitch, 0.7, duration)
            
    fork(chords)
    notes()
    
    performance = s.stop_transcribing()
    performance.to_score(title="RTMP 0.3.5", composer = "Generated with Real Time Midi Program 0.3.5 written by Gabriel Sagan").show_xml()

    sleep_time = random.uniform(4,10)
    
    time.sleep(sleep_time)
    
        
    
    

