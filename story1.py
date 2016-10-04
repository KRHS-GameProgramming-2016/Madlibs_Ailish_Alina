from input import *

#Written by Mr. Spooner
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getNumber("Enter a Number: ")
    
    text = ""
    text += "One day I went to the " + location1
    text += ". It was like a " + temperature1
    text += " out."    
    return text
