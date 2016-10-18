from input import *

#written by ailish

# how to do certain things / mechanics i figured out to use for this
# - initial-getter
# - full name maker


def story():
    
    firstname1 = getWord("Enter a first name: ")
    surname1 = getWord("Enter a last name: ")
    initial1 = surname1[0].upper()
    fullname1 = firstname1 + " " + surname1
    weather1 = getWord("Enter an adjective describing weather: ")
    city1 = getWord("Enter the name of a city: ")
    profession1 = getWord("Enter a profession, like businessman or fisherman: ")
    gender1 = getGender()
    
    subjective = genderMachine(gender1, "subjective")
    objective = genderMachine(gender1, "objective")
    possDeterminer = genderMachine(gender1, "possDeterminer")
    possPronoun = genderMachine(gender1, "possPronoun")
    reflexive = genderMachine(gender1, "reflexive")
    
    firstname2 = getWord("Enter another first name: ")
    surname2 = getWord("Enter another last name: ")
    fullname2 = firstname2 + " " + surname2
    adjective1 = getWord("Enter an adjective: ")
    noun1 = getWord("Enter a noun: ")
    adjective2 = getWord("Enter an adjective: ")
    adjective3 = getWord("Enter an adjective starting with "+initial1 + ": ")
    
    text = ""
    text += "It was a " +weather1
    text += " day in " +city1
    text += " when our story began, and I was on my way to the scene of the crime. The murder of a wealthy " +profession1
    text += ", Mr. " +fullname2
    text += ", had just been reported by the butler at his giant, " +adjective1
    text += " mansion. \n \n When I arrived, the body of Mr. " +surname2
    text += " lay in a pool of blood, a " +noun1
    text += " stabbed into his chest. The butler stood by the body, distraught. " 
    text += "\n\"Who would do such a thing?\" the butler cried. A" +adjective2
    text += " maid stood becide him. "
    text += "\n\"Yes, who? And why?\" she added, seemingly as upset as the butler."
    text += "\n\"I\'ll get to the bottom of this,\" I reassured them. \"They don't call me" +adjective3 + " " +surname1
    text += " for nothing. "
    text += "\n Despite their apparent distress at Mr. " +surname2
    text += "\'s death, I had my suspicions about the butler and the maid."
    text += "\n \n Who should I investigate first? "
    text += "\n\n    A) The butler"
    text += "\n    B) The maid"
    return text

print story()
