from executeCommands import *
import sys

def showMenu1(d,save):
    """
    This function prints in the console the entire menu which contains all the
    available commands the user can introduce.
    input:d-the dictionary , save - and array in which will be saved the dictionary
    before any modification (used for the undo function).
    output: the menu is printed
    """
    str="Please choose one of the following options: \n"
    str+="\t-Press 1 to add an expense to the current day.\n"
    str+="\t-Press 2 to insert an expense to a specific day.\n"
    str+="\t-Press 3 to remove all the expenses in a day.\n"
    str+="\t-Press 4 to remove all the expenses between two days.\n"
    str+="\t-Press 5 to remove all the expenses in a specific category.\n"
    str+="\t-Press 6 to list all the expenses in the current month.\n"
    str+="\t-Press 7 to list all the expenses for a specific day.\n"
    str+="\t-Press 8  to list all the expenses for a specific category with the sum of money spent [ < | = | > ] than a certain value.\n"
    str+="\t-Press 9  to make a total of the expenses for a specific category.\n"
    str+="\t-Press 10 to print the day with the maximum expenses.\n"
    str+="\t-Press 11 to sort the expenses in ascending order by amount of money spent.\n"
    str+="\t-Press 12 to sort the expenses for a specific category in ascending order by amount of money spent.\n"
    str+="\t-Press 13 to keep only expenses in a specific category.  \n"
    str+="\t-Press 14 to keep only expenses in a specific category with amount of money [ < | = | > ] than a certain value.\n"
    str+="\t-Press 15 to undo the last operation.\n"
    str+="\t-Press 16 to print the menu with commands \n"
    str+="\t-Press -1 to return to the main menu \n"
    str+="\t-Press 0 to exit the application \n"
    print(str)
    readCommand1(d, save)

def readCommand1(d, save):
    """
    This function reads the command introduced by the user.
    Until the introduced command is valid, the user is asked to intoduce another command.
    While the command introduced by the user is not "0", the function reads all the commands
    introduced by the user and calls the function for executing the command.
    input: d - the dictionary,save - the list used for saving the dictionary for undo
    output: d, the dictionary after all the changes that took part.
    """
    commands=["-1","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
    cat=["0","1","2","3","4","5","6"]
    categ = ["transport", "internet", "housekeeping", "others", "food", "clothes"]
    s = input("Press 16 to see the list with available commands.\nPlease enter your option:")
    while s not in commands:
        print("\nInvalid option.Please type a digit between 0 and 17.\n")
        s = input("Press 16 to see the list with available commands.\nPlease enter your option:")

    while s!="0":
        if s=="1":
            readAdd(d, cat,save)
        elif s == "2":
            readInsert(d, cat, save)
        elif s=="3":
            readRemoveDay(d, save)
        elif s=="4":
            readRemoveMoreDays(d, save)
        elif s=="5":
            readRemoveCateg(d, save, cat)
        elif s == "6":
            listAll(d, categ, 0)
        elif s == "7":
            readListDay(d, categ)
        elif s == "8":
            listSign(d, cat)
        elif s == "9":
            readSum(d, cat)
        elif s == "10":
            maxDay(d,0)
        elif s == "11":
            sortMonth(d, categ, 0)
        elif s == "12":
            readSortCateg(d, cat)
        elif s=="13":
            readFilterCateg(d, categ, cat, save)
        elif s == "14":
            readFilterSign(d, cat, categ, save)
        elif s == "15":
            d=undoCommand(d, save,0)
        elif s == "16":
            showMenu1(d, save)
            return
        elif s == "-1":
            return

        s = input("\nPress 16 to see the list with available commands.\nPlease enter your option:")
        while s not in commands:
            print("\nInvalid option.Please type a digit between 0 and 17.\n")
            s = input("Press 16 to see the list with available commands.\nPlease enter your option:")

    if s == "0":
        print("\n\tGoodbye! :)\n")
        sys.exit()

def readAdd(d,cat,save):
    """
    This function is used for reading all the needed information for adding an expense to the list.
    For categories, the user is asked to choose from a list that will be printed.Besides that,
    the user must manually introduce the sum of money that must be added.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary, cat-a list with all valid options,save-the list used for saving the dictionary for undo
    Output:the modified dictionary
    """
    print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
    s1 = input("Please choose a category by typing a digit:")
    while s1 not in cat:
        print("\nInvalid option.Please type a digit between 0 and 6.")
        print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
        s1 = input("Please choose a category by typing a digit:")
    if s1 != "0":
        if s1 == "1":
            s1 = "food"
        elif s1 == "2":
            s1 = "internet"
        elif s1 == "3":
            s1 = "transport"
        elif s1 == "4":
            s1 = "clothes"
        elif s1 == "5":
            s1 = "housekeeping"
        else:
            s1 = "others"
        s2 = input("\nType 0 to cancel the command.\nPlease type the sum you want to add:")
        while s2.isdigit() == False:
            print("\nInvalid option.Please type a natural number.\n")
            s2 = input("Type 0 to cancel the command.\nPlease type the sum you want to add:")
        if s2 != "0":
            day = int(findCurrentDay())
            d = insertExpense(str(day), s1, s2, d, save, 0)
    return d

def readInsert(d,cat,save):
    """
    This function is used for reading all the needed information for inserting an expense to the list
    in a specific day.For categories, the user is asked to choose from a list that will be printed.Besides that,
    the user must manually introduce the day and the sum of money that must be added.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary, cat-a list with all valid options,save-the list used for saving the dictionary for undo
    Output:the modified dictionary
    """
    s1 = input("\nType 0 to cancel the command.\nPlease enter the day you want to insert the expense:")
    while s1.isdigit() == False or (int(s1) > 30):
        print("\nInvalid option.Please type a digit between 0 and 30")
        s1 = input("\nType 0 to cancel the command.\nPlease enter the day you want to insert the expense:")
    if s1 != "0":
        print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
        s2 = input("Please choose a category by typing a digit:")
        while s2 not in cat:
            print("\nInvalid option.Please type a digit between 0 and 6.")
            print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
            s2 = input("Please choose a category by typing a digit:")
        if s2 != "0":
            if s2 == "1":
                s2 = "food"
            elif s2 == "2":
                s2 = "internet"
            elif s2 == "3":
                s2 = "transport"
            elif s2 == "4":
                s2 = "clothes"
            elif s2 == "5":
                s2 = "housekeeping"
            else:
                s2 = "others"
            s3 = input("\nType 0 to cancel the command.\nPlease type the sum you want to add:")
            while s3.isdigit() == False:
                print("\nInvalid option.Please type a natural number.\n")
                s3 = input("Type 0 to cancel the command.\nPlease type the sum you want to add. :")
            if s3 != "0":
                d = insertExpense(s1, s2, s3, d, save, 0)
    return d

def readRemoveDay(d,save):
    """
    This function is used for reading all the needed information for removing an entire
    day of expense from the list.The user must manually introduce the day that must be removed.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary,save-the list used for saving the dictionary for undo
    Output:the modified dictionary
    """
    s1 = input("\nType 0 to cancel the command.\nPlease enter the day you want to remove:")
    while s1.isdigit() == False or (int(s1) > 30):
        print("\nInvalid option.Please type a digit between 0 and 30")
        s1 = input("\nType 0 to cancel the command.\nPlease enter the day you want to remove:")
    if s1 != "0":
        removeDay(s1, d, save, 0)
    return d

def readRemoveMoreDays(d,save):
    """
    This function is used for reading all the needed information for removing a sequence of consecutive days of expenses
    from the list.The user must manually introduce the days that are the limits of the sequence.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary,save-the list used for saving the dictionary for undo
    Output:the modified dictionary
    """
    s1 = input("\nType 0 to cancel the command.\nPlease enter the first day:")
    while s1.isdigit() == False or (int(s1) > 30):
        print("\nInvalid option.Please type a digit between 0 and 30")
        s1 = input("\nType 0 to cancel the command.\nPlease enter the second day:")
    if s1 != "0":
        s2 = input("\nType 0 to cancel the command.\nPlease enter the first day:")
        while s2.isdigit() == False or (int(s2) > 30) or (int(s2)<int(s1)):
            if s2.isdigit() == True and (int(s2)<int(s1)):
                print("\nInvalid option.The second day must be greater or equal to the first day.")
                s2 = input("\nType 0 to cancel the command.\nPlease enter the second day:")
            else:
                print("\nInvalid option.Please type a digit between 0 and 30")
                s2 = input("\nType 0 to cancel the command.\nPlease enter the second day:")
        if s2 != 0:
            removeMoreDays(s1, s2, d, save, 0)
    return d

def readRemoveCateg(d,save,cat):
    """
    This function is used for reading all the needed information for removing all the expenses from a specific category
    from the entire month.For categories, the user is asked to choose from a list that will be printed.
    The user must manually introduce the category that must be removed.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary, cat-a list with all valid options,save-the list used for saving the dictionary for undo
    Output:the modified dictionary
    """
    print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
    s1 = input("Please choose a category by typing a digit:")
    while s1 not in cat:
        print("\nInvalid option.Please type a digit between 0 and 6.")
        print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
        s1 = input("Please choose a category by typing a digit:")
    if s1 != "0":
        if s1 == "1":
            s1 = "food"
        elif s1 == "2":
            s1 = "internet"
        elif s1 == "3":
            s1 = "transport"
        elif s1 == "4":
            s1 = "clothes"
        elif s1 == "5":
            s1 = "housekeeping"
        else:
            s1 = "others"
    if s1 != "0":
        removeCategory(s1, d, save, 0)

def readListDay(d,categ):
    """
    This function is used for reading all the needed information for listing all the expenses from a
    The user must manually introduce the day that must be printed.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary, cated-a list with all the categories.
    Output:-
    """
    s1 = input("\nType 0 to cancel the command.\nPlease enter the day you want to see:")
    while s1.isdigit() == False or (int(s1) > 30):
        print("\nInvalid option.Please type a digit between 0 and 30\n")
        s1 = input("Type 0 to cancel the command.\nPlease enter the day you want to see:")
    if s1 != "0":
        list(d, s1, categ, 0)

def listSign(d,cat):
    """
    This function is used for reading all the needed information for printing all the expenses from
    a specific category that are [ < | = | > ] than a specific value.
    For categories, the user is asked to choose from a list that will be printed.
    Besides that,the user must manually introduce the sum of money used for comparisons.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary, cat-a list with all valid options.
    Output:-
    """
    print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
    s1 = input("Please choose a category by typing a digit:")
    while s1 not in cat:
        print("\nInvalid option.Please type a digit between 0 and 6.")
        print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
        s1 = input("Please choose a category by typing a digit:")
    if s1 != "0":
        if s1 == "1":
            s1 = "food"
        elif s1 == "2":
            s1 = "internet"
        elif s1 == "3":
            s1 = "transport"
        elif s1 == "4":
            s1 = "clothes"
        elif s1 == "5":
            s1 = "housekeeping"
        else:
            s1 = "others"
    if s1 != "0":
        print("\n 1 <, 2 =, 3 >, 0-return")
        s2 = input("Please choose a sign by typing a digit:")
        while s2 != "0" and s2 != "1" and s2 != "2" and s2 != "3":
            print("\nInvalid option.Please type a digit between 0 and 3.")
            print("\n 1 <, 2 =, 3 >, 0-return")
            s2 = input("Please choose a sign by typing a digit:")
        if s2 != "0":
            s3 = input("\nType 0 to cancel the command.\nPlease type the sum of money for comparation:")
            while s3.isdigit() == False:
                print("\nInvalid option.Please type a natural number.")
                s3 = input("\nType 0 to cancel the command.\nPlease type the sum of money for comparation:")
            if s3 != "0":
                if s2 == "1":
                    listSmallerThan(d, int(s3), s1, 0)
                elif s2 == "2":
                    listEqual(d, int(s3), s1, 0)
                else:
                    listGreaterThan(d, int(s3), s1, 0)

def readSum(d,cat):
    """
    This function is used for reading all the needed information for printing out the total
    sum of money spent for a specific category over the entire month.
    For categories, the user is asked to choose from a list that will be printed.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary, cat-a list with all valid options.
    Output:-
    """
    print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
    s1 = input("Please choose a category by typing a digit:")
    while s1 not in cat:
        print("\nInvalid option.Please type a digit between 0 and 6.")
        print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
        s1 = input("Please choose a category by typing a digit:")
    if s1 != "0":
        if s1 == "1":
            s1 = "food"
        elif s1 == "2":
            s1 = "internet"
        elif s1 == "3":
            s1 = "transport"
        elif s1 == "4":
            s1 = "clothes"
        elif s1 == "5":
            s1 = "housekeeping"
        else:
            s1 = "others"
    if s1 != "0":
        sum(d, s1, 0)

def readSortCateg(d,cat):
    """
    This function is used for reading all the needed information for  printing out the
    sorted expenses in a specific category over the current month
    For categories, the user is asked to choose from a list that will be printed.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary, cat-a list with all valid options.
    Output:-
    """
    print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
    s1 = input("Please choose a category by typing a digit:")
    while s1 not in cat:
        print("\nInvalid option.Please type a digit between 0 and 6.")
        print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
        s1 = input("Please choose a category by typing a digit:")
    if s1 != "0":
        if s1 == "1":
            s1 = "food"
        elif s1 == "2":
            s1 = "internet"
        elif s1 == "3":
            s1 = "transport"
        elif s1 == "4":
            s1 = "clothes"
        elif s1 == "5":
            s1 = "housekeeping"
        else:
            s1 = "others"
    if s1 != "0":
        sortCateg(d, s1, 0)

def readFilterCateg(d,categ,cat,save):
    """
    This function is used for reading all the needed information for filtering
    all the expenses by only keeping in the dictionary expenses that are in a certain category.
    For categories, the user is asked to choose from a list that will be printed.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary, cat-a list with all valid options,categ -  a list with all the categories,
    save-the list used for saving the dictionary for undo.
    Output:the modified dictionary
    """
    print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
    s1 = input("Please choose a category by typing a digit:")
    while s1 not in cat:
        print("\nInvalid option.Please type a digit between 0 and 6.")
        print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
        s1 = input("Please choose a category by typing a digit:")
    if s1 != "0":
        if s1 == "1":
            s1 = "food"
        elif s1 == "2":
            s1 = "internet"
        elif s1 == "3":
            s1 = "transport"
        elif s1 == "4":
            s1 = "clothes"
        elif s1 == "5":
            s1 = "housekeeping"
        else:
            s1 = "others"
    if s1 != "0":
        d=filterCateg(d, categ, s1, save,0)
    return d

def readFilterSign(d,cat,categ,save):
    """
    This function is used for reading all the needed information for filtering
    all the expenses by only keeping in the dictionary expenses that are in a certain category
    with the sum of money spent for it [< | = | >] than a certain value.
    For categories, the user is asked to choose from a list that will be printed.
    Besides that,the user must manually introduce the sum of money used for comparisons.
    After all the information is received, it is called the function that executes this command.
    Input: d-the dictionary, cat-a list with all valid options,categ -  a list with all the categories.
    save-the list used for saving the dictionary for undo.
    Output:the modified dictionary
    """
    print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
    s1 = input("Please choose a category by typing a digit:")
    while s1 not in cat:
        print("\nInvalid option.Please type a digit between 0 and 6.")
        print("\n 1-food, 2-internet, 3-transport, 4-clothes, 5-housekeeping, 6-others, 0-return")
        s1 = input("Please choose a category by typing a digit:")
    if s1 != "0":
        if s1 == "1":
            s1 = "food"
        elif s1 == "2":
            s1 = "internet"
        elif s1 == "3":
            s1 = "transport"
        elif s1 == "4":
            s1 = "clothes"
        elif s1 == "5":
            s1 = "housekeeping"
        else:
            s1 = "others"
    if s1 != "0":
        print("\n 1 <, 2 =, 3 >, 0-return")
        s2 = input("Please choose a sign by typing a digit:")
        while s2 != "0" and s2 != "1" and s2 != "2" and s2 != "3":
            print("\nInvalid option.Please type a digit between 0 and 3.")
            print("\n 1 <, 2 =, 3 >, 0-return")
            s2 = input("Please choose a sign by typing a digit:")
        if s2 != "0":
            s3 = input("\nType 0 to cancel the command.\nPlease type the sum of money for comparation:")
            while s3.isdigit() == False:
                print("\nInvalid option.Please type a natural number.")
                s3 = input("\nType 0 to cancel the command.\nPlease type the sum of money for comparation:")
            if s3 != "0":
                if s2 == "1":
                    filterSmallerThan(d, int(s3), s1, categ, save,0)
                elif s2 == "2":
                    filterEqual(d, int(s3), s1, categ, save,0)
                else:
                    filterGreaterThan(d, int(s3), s1, categ, save,0)








