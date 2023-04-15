import random
def magicball():
    response = input("Press 'any key' for an answer ans 'q' to quit\n\t What is your question: ")
    magicanswers = [
        "it is certain","You couldn't be more right",
        "Outlook looks good","what would you have me do",
        "You may rely on it","i am not certain that question is for me",
        "Ask again later","i know it's hard now",
        "Concentrate and ask again",
        "reply hazy, try again",
        "My reply is no",
        "my sources says no",
        "You have to keep trying"
        ]
    if response == "q":
        print("have a good day")
        quit()
    else:
        print(random.choice(magicanswers),"\n")
        magicball()
magicball()
