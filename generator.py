from scamp import *
from melody import *
import time
import random

trichord_input()
duration_input()
octaves = octave_input()
temp = tempo_input()

while True:
    
    s = None
    
    if isinstance(temp, list):
        if len(temp) == 2: 
            temp_int = [int(num) for num in temp]
            s = Session(tempo = random.randint(min(temp_int), max(temp_int)))
    else:
        s = Session(tempo = int(temp))
    
    #Use instead if wanting to use external plugin
    #Windows: p = s.new_part("piano")
    #Mac: p = s.new_midi_part("piano", midi_output_device="IAC")
    #Linux: p = s.new_midi_part("piano", midi_output_device="Midi Through Port 0")
    
    p = s.new_midi_part("piano", midi_output_device="loopMIDI Port")
    
    melody = make_melody()
    
    #s.start_transcribing()
    durations = [duration for note, duration in melody]
    notes = [note for note, duration in melody]
    
    sel_rand_dur = random.choice(durations)
    repl_rand_dur = random.choice(durations)
    if random.random() < 0.6:
        durations = [repl_rand_dur if x == sel_rand_dur else x for x in durations]
        
    compound = [0.3333333333333333, 0.6666666666666666, 2]
    simple = [0.25, 0.5, 1, 2]
    
    if all_duration():
        
        meter = None
        
        if random.random() <= 0.3:
            meter = compound
        elif random.random() <= 0.31 <= 0.6:
            meter = simple
    
        if meter:
            new_durations = []
            num_durations = len(durations)
            
            while len(new_durations) < num_durations:
                new_durations.append(random.choice(meter))
                
            durations = new_durations
            
    stepwise_trichords = [[36, 37, 38], [36, 37, 39], [36, 38, 39]]
    triadic_trichords = [[36, 39, 42], [36, 39, 43], [36, 40, 43], [36, 40, 44]]
    diatonic_trichords = [[36, 38, 41], [36, 39, 41], [36, 38, 43]]
    
    if all_trichord():
        
        trichords = None
        
        if random.random() <= 0.1:
            trichords = stepwise_trichords
            octaves = random.choice([[0, 12], [12, 24], [24, 36], [36, 48]])
        elif 0.11 <= random.random() <= 0.2:
            trichords = triadic_trichords
        elif 0.21 <= random.random() <= 0.3:
            trichords = diatonic_trichords
        
        if trichords:
            new_notes = []
            num_notes = len(notes)
            trichord_seq = random.choices(trichords, k=num_notes)
            
            for count in range(len(trichord_seq)):
                random_trichord = trichord_seq[count]
                random_transposition = random.randint(*octaves)
                transposed_trichords = [num + random_transposition for num in random_trichord]
                trichord_seq[count] = transposed_trichords
                
            random.shuffle(trichord_seq)
        
            for trichord in trichord_seq:
                random.shuffle(trichord)
            
            while len(new_notes) < num_notes:
                for trichord in trichord_seq:
                    for note in trichord:
                        if len(new_notes) < num_notes:
                            new_notes.append(note)
                            
            notes = new_notes
    
    melody = list(zip(notes, durations))

    pitch_classes = [(note % 12, duration) for note, duration in melody]   
    
    print(s)
    print(pitch_classes)
    
    if melody:
        for note, duration in melody:
            p.play_note(note, 0.7, duration)
    
    #performance = s.stop_transcribing()
    #performance.to_score(title="RTMP", composer = "Generated with Real Time Midi Program written by Gabriel Sagan").show_xml()

    wait(random.randint(2, 7))

