from input import *

#written by ailish
def story():
    firstname1 = getWord("Enter a first name: ")
    surname1 = getWord("Enter a last name: ")
    fullname1 = firstname1 + " " + surname1
    
    weather1 = getWord("Enter an adjective describing weather: ")
    city1 = getWord("Enter the name of a city: ")
    profession1 = getWord("Enter a profession, like businessman or fisherman: ")
    firstname2 = getWord("Enter another first name: ")
    surname2 = getWord("Enter another last name: ")
    fullname2 = firstname2 + " " + surname2
    adjective1 = getWord("Enter an adjective: ")
    noun1 = getWord("Enter a noun: ")
    adjective2 = getWord("Enter an adjective: ")
    
    
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
    return text

