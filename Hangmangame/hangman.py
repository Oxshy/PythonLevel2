import random
print("HANGMAN GAME")
name=input("Enter your name: ")
print("Good luck",name )
words=["apple","banana","duplex","infinte","seven","tiger","python","java","pattern","complex"]
word=random.choice(words)
#print(word)
print("guess the characters of the word")
guesses=""
turns=10
while turns>0:
    failed=0
    for i in (word):
        if i in guesses:
            print(i)
        else:
            failed+=1
            # print(failed)
            print("-")
    if failed==0:
        print("Congratulations! you win","\n",word)
        break
    guess=input("Guess a character:")
    guesses+=guess
    if guess not in word:
        turns=turns-1
        print("wrong")
        print(turns," guess left")
        if turns==0:
            print("you lose the word was",word, "\n" "better luck next time")

