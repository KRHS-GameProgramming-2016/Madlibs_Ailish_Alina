from splash import *
from input import *
#import therealstory1
import story2
import story3

def madlibs():
    print splash()
    raw_input()
    end = False
    while not end:
        print menu()
        option = getMenuOption()
        if option == "q":
            end = True
        elif option == "1":
            #print story1.story()
            raw_input()
        elif option == "2":
            print story2.story()
            raw_input()
        elif option == "3":
            print story3.story()
            raw_input()
    print "Good Bye!"
    

    
madlibs()
