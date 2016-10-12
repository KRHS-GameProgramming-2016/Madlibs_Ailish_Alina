from input import *

#this was written by Alina Blake. Deal with it, bruh ;)
def story():
    adjective1 = getWord ("Enter a adjective: ")
    temperature1 = getNumber ("Enter a number: ")
    name1 = getWord ("Enter a name for a male: ")
    verb1 = getWord ("Enter a verb: ")
    noun1 = getWord ("Enter a time of day: ")
    adjective2 = getWord ("Enter a texture: ") 
    name2 = getWord ("Enter a name: ")
    noun2 = getWord ("Enter a time of day: ")
    verb2 = getWord ("Enter a verb: ") 
    adjective3  = getWord ("Enter a adjective describing a personality: ")
    verb3  =  getWord ("Enter a verb ending with ing: ")
    noun3 = getWord("Enter a type of building: ")
   
    #text = ""
    #text += "One" +noun2 "," +name2 "randomly decided to" +verb2 "to the most"
    #text += "pequiliar location."  
    #text += "This was the home of a" +adjective3 "creature, the" +adjective1 "unicorn."
    #text += "I could not take my eyes off his" +adjective2 +noun1 ", which"
    #text += "glistened in the artificial light that was provided by a " +temperature1 
    #text += "flatscreen TV. The figures on the screen were" +verb3 ", waging a war of some kind."
    #text += +name1 "looked at me, his soulless eyes as black as dark matter and obsidian's lovechild."
    #text += "They seemed lethal, until"  +name2  "looked at" +name1 "'s headset and mysteriously levitating"
    #text += "Xbox One controller. Dorito dust covered the unicorn's hooves and Mountain Dew bottles were everywhere."
    #text += " \"How does a unicorn play Call of Duty?\"" +name2 "asked themselves, backing away slowly. It was too late."
    #text += +name2 "had seen too much. They backed away from the raging unicorn, hastily returning to their own time."
    #text += "They had time travelled quite enough for one day, they decided. They never wanted to see" +name1 "the"
    #text += "unicorn ever again, online or in person."
    
    text = ""
    text += "One" +noun2
    text += "," +name2
    text += "randomly decided to" +verb1 
    text += "to the most pequiliar location. This was the" +noun3
    text += "of a" +adjective
    text += "creature, the" +adjective1
    text += "unicorn." +name2
    text += "could not take their eyes off his" +adjective2
    text += "textured" +noun1
    text += ",which glistened in the artificial light provided by a" +temperature1
    text += "flatscreen TV. The figures on the screen were" +verb3
    text += ", waging a war of some kind." +name1
    text += "looked at me, his soulless eyes as black as dark matter and obsidian's lovechild. They seemed lethal, until" +name2
    text += "looked at" +name1
    text += "'s levitating Xbox One controller. Dorito dust covered the unicorn's hooves, and Mountain Dew bottles were everywhere." +name2
    text += " shook their head. \ "How does a unicorn play Call of Duty?"\ " +name2
    text += "asked themselves, backing away slowly. It was too late" +name2
    text += "had seen too much. They backed away from the raging unicorn, hastily returning to their own time."
    text += "They had time traveled quite enough for one" +noun2
    text += ", they decided. They never wanted to see" +name1
    text += "the unicorn again, online or in person."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return text
     
print story()
