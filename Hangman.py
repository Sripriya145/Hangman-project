import random

def get_random_word_from_file():
    wordlist=[]
    with open('hangman_wordlist.txt','r') as file:
        wordlist=file.read().split('\n')
        word=random.choice(wordlist)
    return word

def get_letters(word):
    letters=[]
    temp='_'*len(word)
    for char in list(word):
        if char  not in letters:
            letters.append(char)
    character=random.choice(letters)
    for num, char in enumerate(list(word)):
        if character ==char:
            templist=list(temp)
            templist[num]=char
            temp=''.join(templist)
    return temp

def draw_hangman(chances):
    if chances==6:
       print("___________          ")
       print("|         |          ")
       print("|                    ")
       print("|                    ")
       print("|                    ")
       print("|                    ")
    elif chances==5:
        print("___________          ")
        print("|         |          ")
        print("|         0          ")
        print("|                    ")
        print("|                    ")
        print("|                    ")
    elif chances==4:
        print("___________          ")
        print("|         |          ")
        print("|         0          ")
        print("|        /           ")
        print("|                    ")
        print("|                    ")
    elif chances==3:
        print("___________          ")
        print("|         |          ")
        print("|         0          ")
        print("|        /|          ")
        print("|                    ")
        print("|                    ")
    elif chances==2:
        print("___________          ")
        print("|         |          ")
        print("|         0          ")
        print("|        /|\\        ")
        print("|                    ")
        print("|                    ")
    elif chances==1:
        print("___________          ")
        print("|         |          ")
        print("|         0          ")
        print("|        /|\\        ")
        print("|        /           ")
        print("|                    ")
    elif chances==0:
        print("___________          ")
        print("|         |          ")
        print("|         0          ")
        print("|        /|\\        ")
        print("|        / \\        ")
        print("|                    ")

def start_hangman_game():
    Actualword=get_random_word_from_file()
    # print(Actualword)d
    temp=get_letters(Actualword)     
    chances=7
    found=False
    while True:
        if chances==0:
            print(f"sorry dude ☹️   ☹️a! You lost the game. The actualword was : {Actualword} ")
            print("Better luck nexr time")
            break
        print('=== Guess the word ===')
        print(temp,end='')
        print(f"\nthe word length is {len(Actualword)}")
        print(f"Remaining you have a {chances} chances")
        usercharacter=input("Enter the character you think the word may be:")
        if len(usercharacter) >1 and not  usercharacter.isalpha() :
            print("Enter a  valid character")
        else:
            for num,char in enumerate(list(Actualword)):
                if char ==usercharacter:
                    templist=list(temp)
                    templist[num]=char
                    temp=''.join(templist)
                    found=True
        if found ==True:
            found=False
        else:
            chances-=1

        if '_' not in temp:
            print(f"hey hey🤑🤑!! You got the word was :{Actualword}")
            print(f"You got it in {7-chances} guesss")
            break
        else:
            draw_hangman(chances)
        print()

    print("==== Welcome to the Hangman Game ====")
    while True:
        choice=input("Do you want to play agian Yes or No")
        if  'yes' in choice.lower():
            start_hangman_game()
        elif 'no' in choice.lower():
            print("Quitting the Game😟😟")
            break
        else:
            print("Please enter a vaild choice.")


start_hangman_game()