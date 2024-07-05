from trichord_alteration import scramble_trichords
import random

num_notes = 24
num_chords = num_notes / 3
list_of_sum_duration = [] 
def make_melody():
    
    melody = []
    trichords = []
    
    while len(melody) < num_notes:
        
        single_trichord = random.choice(scramble_trichords())
        trichords.append(single_trichord)
        duration_sequence = []
        
        
        #randomly asigns each note a duration
        for note in single_trichord:
            duration = random.choice([.25, .5, 1, 2])
            melody.append([note, duration]) 
            duration_sequence.append(duration)
          
        #adds duration of 3 notes   
        sublist_sum = sum(duration_sequence[:3])
        list_of_sum_duration.append(sublist_sum)
            
            
    return melody, trichords


def make_chord(trichords):
    
    chords = []
    
    global list_of_sum_duration
    
    count = 0
    while count < num_chords:
        chords.append([trichords[count], list_of_sum_duration[count]])
        count += 1
        
    return chords


