from input import *

def story():
    color1 = getWord("Enter a color: ")
    clothing1 = getWord("Enter an article of clothing, like a shirt, scarf, hat, etc.: ")
    food1 = getWord("Enter a type of food, in plural form, as in apples: ")
    animal1 = getWord("Enter an animal: ")
    plant1 = getWord("Enter a plant: ")
    
    
    gender1 = getGender()
    subjective = genderMachine(gender1, "subjective") # SHE danced, HE danced
    objective = genderMachine(gender1, "objective") # i like HER, i like HIM
    possDeterminer = genderMachine(gender1, "possDeterminer") # HER book, HIS book
    possPronoun = genderMachine(gender1, "possPronoun") # the book is HERS, the book is HIS
    reflexive = genderMachine(gender1, "reflexive") # she likes HERSELF, he likes HIMSELF
    BorG = genderMachine(gender1, "BorG") # boy or girl
    
    text = ""
    text += "\n THE TALE OF LITTLE " +color1.upper()
    text += " " +clothing1.upper()
    text += "\n \n There was once a young " +BorG
    text += ", who, clad as always in " +possDeterminer +" favorite " +color1 +" " +clothing1
    text += ", was walking through the forest alone, with only a basket full of " +food1 +". " +subjective.capitalize()
    text += " was making sure to follow very closely to the path, as " +possDeterminer
    text += " mother had instructed. As " +subjective
    text += " travelled along, all of a sudden, a great " +animal1
    text += " stepped out of the trees, and over to " +objective
    text += "."
    text += "\n\"Hello,\" the " +BorG
    text += " cautiously greeted the " +animal1 +"."
    text += "\n\"Why, hello, little " +BorG
    text += ",\", said the " +animal1
    text += ", \"no need to fear. I've only happened to notice that you seem to be ignoring all these beautiful " +plant1
    text += "s! It\'s a shame to pass them by.\""
    text += "\nThe " +BorG
    text += " noticed then that there were dozens and dozens of lovely " +plant1
    text += "s, growing all around " +objective
    text += ", just off the path. "
    text += "\n\"They\'re lovely,\" " +subjective
    text += " replied, \"but I really must follow the path. I\'m bringing my grandmother these " +food1
    text += "s, to better her health.\""
    text += "\n\"Well, wouldn't it be nice to bring her fresh, beautiful " +plant1
    text += "s, to go with them? "
    text += 
    text += 
    
    
    return text
    
print story()
