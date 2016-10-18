def isSwear(word):
    swearList = ["hell",
                 "fuck",
                 "shit",
                 "damn",
                 "piss",
                 "poop",
                 "pee",
                 "jizz",
                 "cum",
            #anatomical:
                 "cock",
                 "dick",
                 "schlong",
                 "penis",
                 "vagina",
                 "pussy",
                 "vulva",
                 "cunt",
                 "genital",
                 "ass",
                 "arse",
                 "anus",
                 "butt",
                 "boob",
                 "breast",
                 
            #offensive:
                "bitch",
                "bastard",
                "whore",
                "slut",
            ]
    if word in swearList:
        return True
    else:
        for i in swearList:
            if i in word:
                return True
        return False

def getMenuOption():
    goodInput = False
    goodResponses = ["1",
                     "2",
                     "3",
                     "q"]
    while not goodInput:
        response = raw_input("Make a selection: ")
        if response.lower() in goodResponses:
            goodInput = True
        else:
            print "Please make a valid selection!"
    return response.lower()

def getWord(prompt):
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if isSwear(response):
            goodInput = False
            print "Don't use that kind of language with me!"
    return response

def getNumber(prompt):
    goodInput = False
    numbers = "0123456789."
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for character in response:
            if character not in numbers:
                goodInput = False
                print "Numbers only please!"
    return response
        
def getGender():
    print "Male or female?: A) Male B) Female"
    goodInput = False
    goodResponses = ["a",
                     "b",
                     "n"]
    while not goodInput:
        response = raw_input("Make a selection: ")
        if response.lower() in goodResponses:
            goodInput = True
        else:
            print "Please make a valid selection!"
            
    return response.lower()

def genderMachine(gender, word):
    
    class female():
        subjective = "she"
        objective = "her"
        possDeterminer = "her"
        possPronoun = "hers"
        reflexive = "herself"
        
    class male():
        subjective = "he"
        objective = "him"
        possDeterminer = "his"
        possPronoun = "his"
        reflexive = "himself"
        
    class neutral():
        subjective = "they"
        objective = "them"
        possDeterminer = "their"
        possPronoun = "theirs"
        reflexive = "themselves"
        
    
    if gender == "a":
        gender = male
    if gender == "b":
        gender = female
    
    if gender == male:
        subjective = male.subjective
        objective = male.objective
        possDeterminer = male.possDeterminer
        possPronoun = male.possPronoun
        reflexive = male.reflexive
        
    if gender == "n":
        subjective = neutral.subjective
        objective = neutral.objective
        possDeterminer = neutral.possDeterminer
        possPronoun = neutral.possPronoun
        reflexive = neutral.reflexive
        
    if gender == female:
        subjective = female.subjective
        objective = female.objective
        possDeterminer = female.possDeterminer
        possPronoun = female.possPronoun
        reflexive = female.reflexive
        
    if word == "subjective":
        return subjective
    if word == "objective":
        return objective
    if word == "possDeterminer":
        return possDeterminer
    if word == "possPronoun":
        return possPronoun
    if word == "reflexive":
        return reflexive













