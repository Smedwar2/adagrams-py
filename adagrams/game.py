from random import randint
    #no parameters 
    #create a letter pool, randomly select 10 letters from the pool, and return them as a list
    #the available letters
    #how frequently each letter appears
    #a way to randomly choose one
    #somewhere to store the 10 letters
def draw_letters():
    hand = []
    letter_pool = ["A", "A", "A", "A", "A", "A", "A", "A", "A", 
                   "B", "B", "C", "C", "D", "D", "D", "D", 
                   "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
                   "F", "F", "G", "G", "G", "H", "H", 
                   "I", "I", "I", "I", "I", "I", "I", "I", "I", "J", "K", 
                   "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N", 
                   "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q",
                   "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", 
                   "T", "T", "T", "T", "T", "T",
                   "U", "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z"]
    #take a copy of the letter pool so we dont modify the original list when we remove letters from it
    working_pool = letter_pool.copy()
    while len(hand) < 10:
    #choose a random position in the working pool 
        random_position = randint(0, len(working_pool) - 1)
    #get the letter at that position
        letter = working_pool[random_position]
    #add letter to empty hand list and remove it from the working pool so it cant be selected again
        hand.append(letter)
        working_pool.pop(random_position)
    return hand









def uses_available_letters(word, letter_bank):
#two parameters: word and letter_bank
#copy the letter bank so we dont modify the original list when we remove letters from it
    working_bank = letter_bank.copy()   
#convert the word to uppercase so we can compare it to the letter bank
    word = word.upper()
#check if input(word) can be formed using only letters from hand
    for letter in word:
        if  letter in working_bank:
            working_bank.remove(letter)
        else:
            return False
    return True
    
    #return True if word can be formed using letters from letter_bank, otherwise return False



















def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass