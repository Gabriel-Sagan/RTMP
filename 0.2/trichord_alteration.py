import random



def scramble_trichords():

    trichords = [ [36, 37, 39], [36, 38, 39], [36, 37, 40], [36, 39, 40], [36, 37, 41], [36, 40, 41], [36, 37, 42], [36, 41, 42],
                  [36, 38, 40],[36, 38, 41], [36, 39, 41], [36, 38, 42], [36, 40, 42], [36, 38, 43],[36, 41, 43], [36, 39, 42],
                  [36, 39, 43], [36, 40, 43],[36, 40, 44] ]

#C2 is 36, Trichord sequence: https://en.wikipedia.org/wiki/List_of_set_classes, Forte No. 3-1 to 3-12

    #shuffles order of trichord and trichords
    random.shuffle(trichords)
    for trichord in trichords:
        random.shuffle(trichord)
        
    #tranposes each trichord to same value

    count = 0

    while count < len(trichords):
    #replaced random_index with count - iterates per item in trichords
        random_trichord = trichords[count]
        random_transposition = random.randint(1, 54)
        transposed_trichords = [num + random_transposition for num in random_trichord]
        trichords[count] = transposed_trichords
        count += 1
         

    return trichords

print(scramble_trichords())




        
            
            
    
            
   
        
        


    

