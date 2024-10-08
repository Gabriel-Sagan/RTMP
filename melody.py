import random

forte_numbers = {
    
    '3-1': [36, 37, 38],
    '3-2': [36, 37, 39],
    '3-2i': [36, 38, 39],
    '3-3': [36, 37, 40],
    '3-3i': [36, 39, 40],
    '3-4': [36, 37, 41],
    '3-4i': [36, 40, 41],
    '3-5': [36, 37, 42],
    '3-5i': [36, 41, 42],
    '3-6': [36, 38, 40],
    '3-7': [36, 38, 41],
    '3-7i': [36, 39, 41],
    '3-8': [36, 38, 42],
    '3-8i': [36, 40, 42],
    '3-9': [36, 38, 43],
    '3-10': [36, 39, 42],
    '3-11': [36, 39, 43],
    '3-11i': [36, 40, 43],
    '3-12': [36, 40, 44]
}

note_values = {
    
    '16th': .25,
    '8th': .5,
    'quarter': 1,
    'half': 2,
    'whole': 4,
    '8th triplet': 0.3333333333333333,
    'quarter triplet': 0.6666666666666666
}

octave_values = {
    
    'C2': 0,
    'C3': 12,
    'C4': 24,
    'C5': 36,
    'C6': 48,
    'C7': 60
}

trichords = []
durations = []
octaves = []

all_trichord = False
all_duration = False

def trichord_input():
    
    global trichords
    global all_trichord
    
    all_trichord = False
    
    while True: 
        selected_chords_str = input("Enter trichord set classes separated by comma. Use i for inverted trichords. (e.g. 3-9, 3-5i, 3-8) or type 'All' for all chords: ")
        
        if selected_chords_str.strip().lower() == 'all':
            trichords = list(forte_numbers.values())
            print(f"Selected All Chords")
            all_trichord = True
            return trichords
        
        selected_chords_list = selected_chords_str.split(',')
        selected_chords_list = [chord.strip() for chord in selected_chords_list]
        
        trichords = list(forte_numbers[num] for num in selected_chords_list if num in forte_numbers)
        
        try:
            if all(chord in forte_numbers for chord in selected_chords_list):
                print(f"Selected Chords: {selected_chords_list}")
                return trichords
            else:
                raise ValueError("Invalid set class input")

        except ValueError as e:
            print(f"{e}, please try again.")
            
def all_trichord():
    global all_trichord
    return all_trichord

def duration_input():
    
    global durations
    global all_duration
    
    all_duration = False
    
    while True:
        selected_duration_str = input("Enter note values separated by comma. (e.g. 16th, 8th, quarter, half, whole, 8th triplet, quarter triplet) or type 'All' for all note values: ")
        
        if selected_duration_str.strip().lower() == 'all':
            durations = list(note_values.values())
            print(f"Selected All Note Values")
            all_duration = True
            return durations
        
        selected_duration_list = selected_duration_str.split(',')
        selected_duration_list = [num.strip() for num in selected_duration_list]
        
        durations = list(note_values[num] for num in selected_duration_list if num in note_values)
        
        try:
            if all(num in note_values for num in selected_duration_list):
                print(f"Selected Note Values: {durations}")
                return durations
            else:
                raise ValueError("Invalid note value input")
            
        except ValueError as e:
            print(f"{e}, please try again.")
            
def all_duration():
    global all_duration
    return all_duration
             
def octave_input():
    
    global octaves
    
    while True:
        try:
            octave_range = input("What should the octave range be between C2 and C7? Please separate by comma (e.g. C2, C4): ").upper()
            octave_range = octave_range.split(',')
            octave_range = [num.strip() for num in octave_range]
            
            octaves = list(octave_values[num] for num in octave_range if num in octave_values)
            
            if len(octaves) == 2:
                if octaves[0] < octaves[1]:                          
                    print(f"Selected octave range: {octave_range}")
                    return octaves
                else:
                    raise ValueError("The first octave must be less than the second octave.")
            else:
                raise ValueError("Please enter exactly two octaves starting on C separated by a comma.")
                
        except ValueError as e:
            print(f"{e} Please try again.")
            
def tempo_input():

    while True:
        
        choice = input("Should there be a random tempo selected? (Y/N): ").lower()
        if choice == 'y' or choice == 'yes':
            while True:
                try:
                    tempo_range = input("What should the tempo range be? Please separate by comma (e.g. 60, 75): ")
                    tempo_range = tempo_range.split(',')
                    tempo_range_int = [int(num.strip()) for num in tempo_range]
                    
                    if len(tempo_range_int) == 2:
                        if tempo_range_int[0] < tempo_range_int[1]:                          
                            print(f"Tempo range: {tempo_range_int}")
                            return tempo_range_int
                        else:
                            raise ValueError("The first number must be less than the second number.")
                    else:
                        raise ValueError("Please enter exactly two numbers separated by a comma.")
                        
                except ValueError as e:
                    print(f"{e} Please try again.")
        
        elif choice == 'n' or choice == 'no':
            
            while True:  
                tempo = input("Enter the tempo to be used: ")
                
                try:   
                    if int(tempo):
                        print(f'Selected BPM = {tempo}')
                        return tempo
                        
                    else:
                        raise ValueError("Invalid input")
                        
                except ValueError as e:
                    print(f"{e}, please try again.")
        else:
            print('Please input Y/N')
    

def note_input():
    
    while True:
        
        choice = input("Should there be random number of notes selected? (Y/N): ").lower()
        if choice == 'y' or choice == 'yes':
            while True:
                try:
                    note_range = input("What should the note number range be? Please separate by comma (e.g. 6, 36): ")
                    note_range = note_range.split(',')
                    note_range_int = [int(num.strip()) for num in note_range]
                    
                    if len(note_range_int) == 2:
                        if note_range_int[0] < note_range_int[1]:                          
                            print(f"Note number range: {note_range_int}")
                            return note_range_int
                        else:
                            raise ValueError("The first number must be less than the second number.")
                    else:
                        raise ValueError("Please enter exactly two numbers separated by a comma.")
                        
                except ValueError as e:
                    print(f"{e} Please try again.")
        
        elif choice == 'n' or choice == 'no':
            
            while True:  
                note = input("Enter the number of notes: ")
                
                try:   
                    if int(note):
                        print(f'Selected number = {note}')
                        return note
                        
                    else:
                        raise ValueError("Invalid input")
                        
                except ValueError as e:
                    print(f"{e}, please try again.")
        else:
            print('Please input Y/N')
            

notes = note_input()

def note_num_check():
    
    if isinstance(notes, list):
        if len(notes) == 2:
            notes_int = [int(num) for num in notes]
            random_int = random.randint(min(notes_int), max(notes_int))
            return random_int
                
    else:
        return int(notes)
            

def make_melody():
    
    melody = []
     
    num_notes = note_num_check()
            
    trichord_seq = random.choices(trichords, k=num_notes)
    
    for count in range(len(trichord_seq)):
        random_trichord = trichord_seq[count]
        random_transposition = random.randint(*octaves)
        transposed_trichords = [num + random_transposition for num in random_trichord]
        trichord_seq[count] = transposed_trichords
    
    random.shuffle(trichord_seq)
    
    for trichord in trichord_seq:
        random.shuffle(trichord)
        
    while len(melody) < num_notes:
        for trichord in trichord_seq:
            for note in trichord:
                if len(melody) < num_notes:
                    duration = random.choice(durations)
                    melody.append([note, duration])
        
    return melody
    
