from input import *

#written by ailish
def story():
    firstname1 = getWord("Enter a first name: ")
    lastname1 = getWord("Enter a last name: ")
    
    weather1 = getWord("Enter an adjective describing weather: ")
    city1 = getWord("Enter the name of a city: ")
    profession1 = getWord("Enter an adjective describing a job of profession: ")
    
    
    text = ""
    text += "It was a " +weather1
    text += " day in " +city1
    text += " when our story began, and I was on my way to the scene of the crime. The murder of a wealthy " +profession1
    
    return text

