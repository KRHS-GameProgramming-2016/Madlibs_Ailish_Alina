from input import *


def story ():
    
    gender1 = getGender()
    subj = genderMachine(gender1, "subjective")
    obj = genderMachine(gender1, "objective")
    possDet = genderMachine(gender1, "possDeterminer")
    possPron = genderMachine(gender1, "possPronoun")
    reflex = genderMachine(gender1, "reflexive")
    
    text = ""
    text += "In the evening after they had gone again to the ball, the Fairy Godmother made her appearance. "
    text += "Once more Cinderella drove to the Palace in " +possDet
    text += " coach and six; this time arrayed in a still more gorgeous and beautiful dress; "
    text += "and once more the Prince danced with " +obj
    text += " all the evening. But when the third night came Cinderella was enjoying " +reflex
    text += " so much that "+subj
    text += " quite forgot what " +possDet
    text += " Fairy Godmother had said, until suddenly " +subj
    text += " heard the clock begin to strike twelve. "
    return text
    
print story()
