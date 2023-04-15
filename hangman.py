import random #time moudle is imported to make use of the systems time
    
user = input("enter your name: ")
print("\t\tWelcome",user,"\n\t\t===============\nSelect an option from the main menu")

main_menu = ("\tMain Menu\n\t=========\n1. Play Game\n2. Veiw Instructions\n3. End game")
print(main_menu)
option = int(input("\tSelect an option: "))
print("\t---------------")
if option == 1:
    print("1. Beginner\n2. Advance\n3. Expert\n4. Go back to main menu")
elif option == 2:
    print("Welcome to my Hangman Game!, It took me a very long time to create and i didnt sleep till 12am,\nI wanted to ensure i got it right cos it inrigued me a lot,i searched online but met only a few examples about how to write hang man game in python but those examples used classes and functions and i didnt think i would be able to write it out of those classes and functions but i read them then started some  ")
elif option == 3:
    print("Come back later")
    quit()
lvl_opts = int(input("Select a level \tOr back to Main Menu: "))
if lvl_opts == 1:
    word = "december" #['december','events','salary']
    #word = random.choice(words)#to pick a word in words at random
    #print("Guess the characters")
    guesses = '' #initialize the guesses
    turns = 5 #number of trials the player should have
    while turns > 0:
        failed = 0 #initialize the number of fails
        for char in word:#check for the characters in word
            if char in guesses:#check for the guess in the character 
                print(char)
            else:
                print("_")
                failed += 1 #increment failure
        if failed == 0:#if the user gets the word at the first trial
            print("You Win")
            print("The word is: ",word.title())
            break
        guess = input("Guess a letter: ")
        guesses += guess
        if guess not in word:
            turns -= 1#decrement the number of trials
            print("Wrong")
            print("You have ", + turns," more chances for wrong guesses")
            if turns == 0:#when the user runs out of trilas after it has reduced 0
                print("You Loose")
                quit()#this is a function used to close the idle 
elif lvl_opts == 2:
    words = ['december','january','febuary','march','april','may','june','july','august','september','october','november']
    word = random.choice(words)#to pick a word in words at random
    print("You have four words to guess from\nThe collective word to guess from is months")
    guesses = '' #initialize the guesses
    turns = 3 #number of trials the player should have
    while turns > 0:
        failed = 0 #initialize the number of fails
        for char in word:#check for the characters in word
            if char in guesses:#check for the guess in the character 
                print(char)
            else:
                print("_")
                failed += 1 #increment failure
        if failed == 0:#if the user gets the word at the first trial
            print("You Win")
            print("The word is: ",word.title())
            break
        guess = input("Guess a character: ")
        guesses += guess
        if guess not in word:
            turns -= 1#decrement the number of trials
            print("Wrong")
            print("You have ", + turns," more guesses")
            if turns == 0:#when the user runs out of trilas after it has reduced 0
                print("You Loose")
                quit()
elif lvl_opts == 3:
    print("")
elif lvl_opts == 4:
    main_menu = ("\tMain Menu\n\t=========\n1. Play Game\n2. Veiw Instructions\n3. End game")
    print(main_menu)
x = 0
while x < 5:
    main_menu = ("\tMain Menu\n\t=========\n1. Play Game\n2. Veiw Instructions\n3. End game")
    #print(main_menu)
    option = int(input("\tselect an option: "))
    print("\t---------------")
    if option == 1:
        print("1. Beginner\n2. Advance\n3. Expert\n4. Go back to main menu")
    elif option == 2:
        print(" ")
    elif option == 3:
        print("Come back later")
        quit()
    lvl_opts = int(input("Select a level \tOr back to Main Menu: "))
    if lvl_opts == 1:
        word = "december" 
        guesses = '' 
        turns = 3 
        while turns > 0:
            failed = 0
            for char in word:
                if char in guesses:
                    print(char)
                else:
                    print("_")
                    failed += 1
            if failed == 0:
                print("You Win")
                print("The word is: ",word.title())
                break
            guess = input("Guess a letter: ")
            guesses += guess
            if guess not in word:
                turns -= 1
                print("Wrong")
                print("You have ", + turns," more guesses")
                if turns == 0:
                    print("You Loose")
    elif lvl_opts == 2:
        words = ['december','january','febuary','march','april','may','june','july','august','september','october','november']
        word = random.choice(words)
        print("You have four words to guess from\nThe collective word to guess from is months")
        guesses = '' 
        turns = 3 
        while turns > 0:
            failed = 0 
            for char in word:
                if char in guesses: 
                    print(char)
                else:
                    print("_")
                    failed += 1
            if failed == 0:
                print("You Win")
                print("The word is: ",word.title())
                break
            guess = input("Guess a character: ")
            guesses += guess
            if guess not in word:
                turns -= 1
                print("Wrong")
                print("You have ", + turns," more guesses")
                if turns == 0:
                    print("You Loose")
                    quit()
    elif lvl_opts == 3:
        print("")
    elif lvl_opts == 4:
        main_menu = ("\tMain Menu\n\t=========\n1. Play Game\n2. Veiw Instructions\n3. End game")
        print(main_menu)
    
