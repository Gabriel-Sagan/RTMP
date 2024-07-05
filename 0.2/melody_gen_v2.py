from trichord_alteration import scramble_trichords
import random

def make_melody():
    
    melody = []
    num_notes = random.randint(7,30)
    
    while len(melody) < num_notes:
        single_trichord = random.choice(scramble_trichords())
        for note in single_trichord:
            duration = random.choice([.25, 0.5, 1, 1.5, 2])
            melody.append([note, duration])
            
    return melody


            
            
            
