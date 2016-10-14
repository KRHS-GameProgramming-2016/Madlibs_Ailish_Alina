from input import *

#this was written by Alina Blake. Deal with it, bruh ;)
def story():
  
    adjective1 = getWord("Enter an adjective: ")
    adjective2 = getWord("Enter a texture ending in ly: ")
    adjective3 = getWord("Enter an adjective describing a personality: ") 
    name1 = getWord("Enter a name for a male: ")
    name2 = getWord("Enter a name that is not name1: ")
    noun1 = getWord("Enter a unicorn's body part: ")
    noun2 = getWord("Enter a time of day: ")
    noun3 = getWord("Enter a type of building, lair, general location, object in outer space, or type of room: ")
    verb1 = getWord("Enter a verb: ")
    verb2 = getWord("Enter a verb that is not verb1 ending in ing: ")
    verb3 = getWord("Enter verb1 in past tense ending in ing: ")
    verb4 = getWord("Enter verb1 ending in ed: ")
    measurement1 = getNumber("Enter a number: ")
    
    text = ""
    text += "One" +noun2
    text += "," +name2
    text += "randomly decided to" +verb1 
    text += "to the most pequiliar location. This was the" +noun3
    text += "of a" +adjective3
    text += "creature, the" +adjective1
    text += "unicorn." +name2
    text += "could not take their eyes off his" +adjective2
    text += "textured" +noun1
    text += ",which glistened in the artificial light provided by a" +measurement1
    text += "flatscreen TV. The figures on the screen were" +verb2
    text += ", waging a war of some kind." +name1
    text += "looked at me, his soulless eyes as black as dark matter and obsidian's lovechild. They seemed lethal, until" +name2
    text += "looked at" +name1
    text += "'s levitating Xbox One controller. Dorito dust covered the unicorn's hooves, and Mountain Dew bottles were everywhere." +name2
    text += " shook their head. \"How does a unicorn play Call of Duty?\"" +name2
    text += "asked themselves, backing away slowly. It was too late" +name2
    text += "had seen too much. They backed away from the raging unicorn, hastily " +verb3
    text += "the" +noun3 
    text += "They had" +verb4
    text += "quite enough for one" +noun2
    text += ", they decided. They never wanted to see" +name1
    text += "the unicorn again, online or in person."
    return text
     
print story()
