word = "aaabbcccd"
chars = set(['b', 'd'])

def compute_difficulty(word, chars):
    
    characterList = list(word)
    print(characterList)
    counter = 0

    for character in characterList:
        for char in chars:
            print(char)
            if character == char:
                counter +1
            else:
                pass
    
    return counter

print(compute_difficulty(word, chars))