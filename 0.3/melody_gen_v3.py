from trichord_alteration import scramble_trichords
import random

num_notes = random.randint(7,30)
num_chords = num_notes / 3
list_of_sum_duration = [] #global

def make_melody():
    
    melody = []
    
    while len(melody) < num_notes:
        
        duration_sequence = []
        single_trichord = random.choice(scramble_trichords())
        
        #randomly asigns each note a duration
        for note in single_trichord:
            duration = random.choice([1, 2])
            melody.append([note, duration]) 
            duration_sequence.append(duration)
          
        #adds duration of 3 notes   
        sublist_sum = sum(duration_sequence[:3])
        list_of_sum_duration.append(sublist_sum)
            
            
    return melody


def make_chord():
    
    chords = []
    
    global list_of_sum_duration
    
    count = 0
    while count < num_chords:
        single_trichord = random.choice(scramble_trichords())
        chords.append([single_trichord, list_of_sum_duration[count]])
        count += 1
        
    return chords


