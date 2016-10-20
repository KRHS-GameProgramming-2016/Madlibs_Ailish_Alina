from input import *

#written by ailish and mercilessly edited by Alina

# how to do certain things / mechanics i figured out to use for this
# - initial-getter
# - full name maker

#def story():
    #beginning()
    #MAKEACHOICE()
    #MaidStory()
    #ButlerStory()
    #return text
#print story

def story():
    
    firstname1 = getWord("Enter a first name: ")
    surname1 = getWord("Enter a last name: ")
    initial1 = surname1[0].upper()
    fullname1 = firstname1 + " " + surname1
    weather1 = getWord("Enter an adjective describing weather: ")
    city1 = getWord("Enter the name of a city: ")
    profession1 = getWord("Enter a profession, like businessman or fisherman: ")
    victimfirst = getWord("Enter another first name: ")
    victimsur = getWord("Enter another last name: ")
    victimfull = victimfirst + " " + victimsur
    adjective1 = getWord("Enter an adjective: ")
    noun1 = getWord("Enter a noun: ")
    adjective2 = getWord("Enter an adjective: ")
    adjective3 = getWord("Enter an adjective starting with "+initial1 + ": ")
    

    text = ""
    text += "It was a " +weather1
    text += " day in " +city1
    text += " when our story began, and I was on my way to the scene of the crime. The murder of a wealthy " +profession1
    text += ", Mr. " +victimfull
    text += ", had just been reported by the butler at his giant, " +adjective1
    text += " mansion. \n \n When I arrived, the body of Mr. " +victimsur
    text += " lay in a pool of blood, a " +noun1
    text += " stabbed into his chest. The butler stood by the body, distraught. " 
    text += "\n\"Who would do such a thing?\" the butler cried. A" +adjective2
    text += " maid stood becide him. "
    text += "\n\"Yes, who? And why?\" she added, seemingly as upset as the butler."
    text += "\n\"I\'ll get to the bottom of this,\" I reassured them. \"They don't call me" +adjective3 + " " +surname1
    text += " for nothing. "
    text += "\n Despite their apparent distress at Mr. " +victimsur
    text += "\'s death, I had my suspicions about the butler and the maid."
    text += "\n \n Who should I investigate first? "
    text += "\n\n  A) The butler"
    text += "\n  B) The maid \n"
    print text
    choice = getSuspectOption()
    if choice == "a":
        print ButlerStory(victimfirst, victimsur)
    if choice == "b":
        print MaidStory(victimfirst, victimsur)

def getSuspectOption():
    goodInput = False
    goodResponses = ["a",
                    "b",]
    while not goodInput:
        response = raw_input("Please choose to investigate the butler (A), or the maid (B): ")
        if response.lower() in goodResponses:
            goodInput = True
        else:
            print "Please make a valid selection!"
    return response.lower()

def MaidStory(victimfirst, victimsur):
    victimfull = victimfirst + " " + victimsur
   
    text = "\n"
    text += "I decided to investigate the maid first. " +victimfull
    return text

def ButlerStory(victimfirst, victimsur): 
    victimfull = victimfirst + " " + victimsur
    
    text = "\n"
    text += "I decided it wise to investigate the butler first. " +victimfull
    return text

story()
