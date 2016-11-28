from executeCommands import *
import sys

def showMenu(d,save):
    """
    This function prints in the console the entire menu,
    which contains all the available commands the user can introduce.
    input:d-the dictionary, save - and array in which will be saved the dictionary
    before any modification (used for the undo function).
    output: the menu is printed
    """
    str="\n There is a list of available commands: \n"
    str+="\t • add <sum> <category> - to the current day \n"
    str+="\t • insert <day> <sum> <category> \n"
    str+="\t • remove <day>  \n"
    str+="\t • remove <start day> to <end day> \n"
    str+="\t • remove <category> \n"
    str+="\t • list <day> \n"
    str+="\t • list \n"
    str+="\t • list <category> [ < | = | > ] <value> \n"
    str+="\t • sum <category>  \n"
    str+="\t • max day  \n"
    str+="\t • sort day  \n"
    str+="\t • sort <category>  \n"
    str+="\t • filter <category>  \n"
    str+="\t • filter <category> [ < | = | > ] <value>  \n"
    str+="\t • undo  \n"
    str+="\t • menu or help \n"
    str+="\t • return \n"
    str+="\t • exit \n"
    print(str)
    readCommand(d,save)

def readCommand(d,save):
    """
    This function reads the command introduced by the user.
    The command is splitted so that every word is placed in a different position of a list.
    While the command introduced by the user is not "exit", the function reads all the commands
    introduced by the user and calls the function for executing the command.
    @ Multiple spaces are not being taken into consideration
    input: d, the dictionary,save - and array in which will be saved the dictionary
    before any modification (used for the undo function).
    output: d, the dictionary after all the changes that took part
    """
    categ = ["transport", "internet", "housekeeping", "others", "food", "clothes"]
    x = input("Enter your command: ")
    x = " ".join(x.split())
    a = []
    a = x.split(" ")
    while a[0]!="exit" or (a[0]=="exit" and len(a)!=1):
        while verifyCommand(a, categ,0)==False:
            x = input("Enter your command: ")
            x = " ".join(x.split())
            a = []
            a = x.split(" ")
        if a[0]=="return":
            return
        elif a[0] == "menu" or a[0] == "help":
            showMenu(d, save)
            return
        elif (a[0] == "exit"):
            print("\n\tGoodbye! :)")
            sys.exit()
        else:
            d = executeCommand(d, a, categ, save)
        x = input("\nEnter your command: ")
        x = " ".join(x.split())
        a = []
        a = x.split(" ")
    if (a[0] == "exit"):
        print("\n\tGoodbye! :)")
        sys.exit()












