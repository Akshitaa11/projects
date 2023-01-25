# randomly chose a word from the list
import random 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game =False
word_list=["waste","public","host","biscuit"]
chosen_word =random.choice(word_list)
word_length =len(chosen_word)

#set lives
lives= 6 

#print(f' the solution is {chosen_word}')

display = []
for _ in range(word_length) :
    display += "_"
    

# ask the user to guess the word .make the guess lowercase
while  not end_of_game :
    guess=input("Guess the letter : ").lower()

# check the guessed letter is correct
    for position in range (word_length) :
       letter = chosen_word[position]
    #print(f'Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}')
       if letter == guess:
          display[position]= letter     


    if guess not in chosen_word:
        lives-=1
        if lives ==0:
          end_of_game=True 
          print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you win.")

    print(stages[lives])
