from commandBasedUI import *
from menuBasedUI import *
from executeCommands import *
import sys

def printOptions():
    """
    This function is used for printing in the console the three available options for the user.
    Then it is called the function that reads what the user is introducing.
    input:-
    output:The menu with available commands is printed.
    """
    str = "\n Hello! Please choose an option: \n"
    str += "\t • Press 1 for command-based UI \n"
    str += "\t • Press 2 for menu-based UI \n"
    str += "\t • Press 0 to exit \n"
    print(str)
    readOption()

def readOption():
    """
    This function is used for reading the command from the user.The user must choose between command-based UI
    and menu-based UI.Then, until the command is valid, the user is asked to introduce a valid command.
    While the introduced command is not "0" ,  it is called the function that reads the specific command in each module.
    Input:-
    Output:-
    """
    x = input("Please enter your option:")
    while verifyOption(x,0) == False:
        x = input("Please enter your option:")
    while x!="0":
        if x == "1":
            showMenu(d, save)
        elif x == "2":
            showMenu1(d, save)
        printOptions()

    print("\n\tGoodbye! :)\n")
    sys.exit()

d={}
save=[]
test(d,save)
save=[]
itemsForTest(d)
printOptions()