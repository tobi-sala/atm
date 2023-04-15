#import modlue first
from tkinter import *

#create a display window
root = Tk()
root.geometry("300x300")
root.title("Mad Lib Generator")

Label(root, text = "Mad Libs Generator \n Have Fun!!!", font = "arial 20 bold ").pack()
Label(root, text = "click any one you want: ", font = "arial 15 bold").place(x=40, y=80)

def madlib1():
    animals = input("Enter the nameof an animal: ")
    profession = input("Enter a profession: ")
    cloth = input("Enter a piece of cloth: ")
    thing = input("Enter a name of a thing: ")
    place = input("Enter a name of a place: ")
    verb = input("Enter a verb ending with 'ing': ")
    food = input("Enter the name of a food: ")
    name = input("Enter a name: ")

    story1 = "say " + food + ", the potographer said as the camera flashed! " + name + "\
            and i had gone to " + place + " to get our photos taken on my birthday.\
            The first photo we really wanted was a picture of us dressed as " + animals + "\
            pretending to be a " + profession + ". When we saw the second photo, it was exactly\
            what i waned. We both looked like " + thing + " wearing " + cloth + "\
            and " + verb + " --exactly what i had in mind"
    print(story1)

def madlib2():
   
    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')

    story2 = 'Last night I dreamed I was a ' +adjactive+ ' butterfly with \
            ' + color+ ' splocthes that looked like '+thing+ ' .I flew to \
            ' + place+ ' with my bestfriend and '+person+ ' who was a \
            '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there\
            and then decided to '+verb+ ' and the dream ended when I said-- lets \
            ' +verb+ '.'
    print(story2)


def madlib3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')

   
    story3 = 'Today we picked apple from '+person+ "'s Orchard. I had no idea \
            there were so many different varieties of apples. I ate " +color+ '\
            apples straight off the tree that tested like '+foods+ '. Then there\
            was a '+adjective+ ' apple that looked like a ' + thing + '.When our\
            bag were full, we went on a free hay ride to '+place+ ' and back. \
            It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. \
            I can hardly wait to get home and cook with the apples. We are going\
            to make appple '+food+ ' and '+things+' pies!.'
    print(story3)

Button(root, text = "the Photorapher", font = "arial 15", command = madlib1, bg = "ghost white").place(x=60, y=120)
Button(root, text = "apple and apple", font = "arial 15", command = madlib2, bg = "ghost white").place(x=70, y=180)
Button(root, text = "the butterfly ", font = "arial 15", command = madlib3, bg = "ghost white").place(x=80, y=240)


root.mainloop()

print("-----------------------------------------------------------------------------------------------")

name = input("What is the name of this genius: ")
story = "Most doctors agree that bicycles of ______ is an ______\
form of exercise. ______ a bicycle enables your to develop your ______\
muscles as well as ______ increases the rate of a ______ beat. More ______\
around the world ______ bicycles than drive ______ No matter what kind of \
______ you ______, always be sure to wear a/an ______ helmet. Make sure to \
have ______ reflectors too!"

print("Hello ", name, " This is the story which you are to complete")
print(story)

'''word1 = input("Enter a word of your choice and press enter: ")
word2 = input("Enter a word of your choice and press enter: ")
word3 = input("Enter a word of your choice and press enter: ")
word4 = input("Enter a word of your choice and press enter: ")
word5 = input("Enter a word of your choice and press enter: ")
word6 = input("Enter a word of your choice and press enter: ")
word7 = input("Enter a word of your choice and press enter: ")
word8 = input("Enter a word of your choice and press enter: ")
word9 = input("Enter a word of your choice and press enter: ")
word10 = input("Enter a word of your choice and press enter: ")
word11 = input("Enter a word of your choice and press enter: ")
word12 = input("Enter a word of your choice and press enter: ")
word13 = input("Enter a word of your choice and press enter: ")'''

verb1 = input("Enter a verb of your choice and press enter: ")
adj1 = input("Enter an adjective of your choice and press enter: ")
verb2 = input("Enter a verb of your choice and press enter: ")
body_part = input("Enter a body part name of your choice and press enter: ")
adverb = input("Enter an adverb of your choice and press enter: ")
body_part2 = input("Enter a body part name of your choice and press enter: ")
noun = input("Enter a noun of your choice and press enter: ")
verb3 = input("Enter a verb of your choice and press enter: ")
animal = input("Enter an animal of your choice and press enter: ")
noun2 = input("Enter a noun of your choice and press enter: ")
verb4 = input("Enter a verb of your choice and press enter: ")
adj2 = input("Enter an adjective of your choice and press enter: ")
color = input("Enter a color of your choice and press enter: ")


story = "Most doctors agree that bicycles of " + verb1 + " is an " + adj1 + "\
form of exercise. " + verb2 + " a bicycle enables your to develop your "\
+ body_part + " muscles as well as " + adverb + " increases the rate of a"\
+ body_part2 + " beat. More " + noun + "around the world " + verb3 + "\
bicycles than drive " + animal + ". No matter what kind of " + noun2 +"\
you " + verb4 + ", always be sure to wear a/an " +adj2 + " helmet. Make\
sure to have " + color + " reflectors too!"

print(story)
        
        
