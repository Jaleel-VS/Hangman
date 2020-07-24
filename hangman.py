import random, sys

print("H A N G M A N")
lista = ['python', 'java', 'kotlin', 'javascript']

while True:
    random.seed()
    word = random.choice(lista)
    size = len(word)
    hidden = size*"-"
    tries = 8
    already_typed = set()
    
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ')
        if choice == 'play':
            break
        if choice == 'exit':
            sys.exit()

    while True:    
        
        print("\n"+hidden)
        guess_letter = input("Input a letter: ")

        
        if guess_letter in already_typed:
            print("You already typed this letter")        

        elif len(guess_letter)>1:
            print("You should input a single letter")
        
        elif not guess_letter.isalpha() or not guess_letter.islower():
            print("It is not an ASCII lowercase letter")

        elif guess_letter in word:       
            for char in range(size):
                if word[char] == guess_letter:                
                    hidden = hidden[:char] + guess_letter + hidden[char + 1:]
            already_typed.add(guess_letter)
                

        else:
            already_typed.add(guess_letter)
            print("No such letter in the word")
            tries -= 1
            
        
        if word == hidden:
            print("You guessed the word! \nYou survived!")
            break
        if tries == 0:
            print("You are hanged!")
            break
    print()
