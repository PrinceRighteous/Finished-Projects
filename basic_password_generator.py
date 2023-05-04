#THIS PROJECT TOOK 4 days to complete!!
### FOR SOME REASON PASSWORDS DONT PRINT EVERY TIME BUT THE CODE IS RIGHT AND WORKS DON"T CHANGE TOO MUCH IF ANYTHING AT ALL!!! ########


import random as r

chars = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%&*")
password_count = int(input("How many passwords do you want? place a number: "))
password_len = int(input("How long would you like your password to be? place a number: "))


def pass_generator(whole):
    while whole:
        password_count = int(input("How many passwords do you want? place a number: "))
        password_len = int(input("How long would you like your password to be? place a number: "))
        for t in range(0,password_count):
            pass_w = ""
            for y in range(0,password_count): # code won't create the amount of passwords as the password count:
                pass_w += r.choice(chars * password_len)
                if len(pass_w) == password_len:
                    print(f"This is your password : {(pass_w)} ")
        final_quest = input("do you wish to create more passwords, type Yes or No?: ")
        if final_quest == "Yes":
                whole = True
        elif final_quest == "No":
            whole = False
            return "these are your passwords!"
        else:
            whole = False
            return "these are your passwords!"

print(pass_generator(True))

##### PROBLEMZ WE FIXED AND HOW WE FIXED IT!!!! ###########
#need to stop whole loop from running forever #fixed with whole variable
#need password to randomly produce multiple letters #fixed with second for loop.
#need to stop whole loop after for loop has ran the amount of times as we put in the password_count #fixed with final quest if statements
#need to stop whole loop after for loop has ran the amount of times as we put in the password_count
# for x in range(0, password_count): #making the same password show the amount of times as the password count, we want a different password each time #fixed with for loop over all code the t for loop to be exact!