from input import *

#Written by Alina Blake
def story():
    size1 = getWord("Enter a word that describes the overall size of a canine figure: ")
    dogbreed1 = getWord("Enter a dog breed: ")
    texture1 = getWord("Enter a texture of the ground: ")
    
    gender1 = getGender()
    subjective = genderMachine(gender1, "subjective") # SHE danced, HE danced
    objective = genderMachine(gender1, "objective") # i like HER, i like HIM
    possDeterminer = genderMachine(gender1, "possDeterminer") # HER book, HIS book
    possPronoun = genderMachine(gender1, "possPronoun") # the book is HERS, the book is HIS
    reflexive = genderMachine(gender1, "reflexive") # she likes HERSELF, he likes HIMSELF

#story()

The *size* *dog breed* trotted along the alleyway, paws hardened after walking along 
hard, brittle surfaces for too long. As *he/she/they if youre obsessed with
gender neutral pronouns* reached the end of their little, private path, bright
lights assaulted their eyes. *gender* always hated emerging onto a bustling sidewalk.
It was always challenging for them to walk down *generic street name* Avenue, they jumped, 
bobbed, and wove between legs. It was like *popular TV show* (preferrably not wipeout or 
american ninja warrior), except that you were little over *super small height that should
not make sense*. Life was a challenge, to say the least. 

text = ""
text += "The" +size1
text += +dogbreed1 "trotted along the alleyway, paws hardened after walking along"
text += +texture1 "streets for too long. As" +subjective 
text += " *words go here* "
