import random
import words as w


word = random.choice(w.words_list)

errors = 6
guessess = []
done = False

while not done: #not keyword changes the boolean value to the opposite of what it already is so in this case the False for done is now True
    for letter in word:
        if letter.lower() in guessess: #the lower() function ensures that even if our word has uppercase letters they will be made lowercase to match our lowercase guess.
            print(letter, end=" ") #we use the end keyword to make a space between each letter to ensure each letter dosen't make a newline when we print them out
        else:
            print("_", end=" ")
    print("")

    if errors == 6:
        guess = input(print(f"Lets begin, your allowed errors are {errors}.: "))
    else:
        guess = input(f"Allowed errors left {errors}, Next guess come on!!!!: ")
        guessess.append(guess.lower())
    if guess.lower() not in word.lower():
        errors -= 1
        if errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guessess:
            done = False

if done:
    print("good job you won!!!")
else:
    print(f"you lost!!!, The word was {word}.")