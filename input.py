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
        
        



















