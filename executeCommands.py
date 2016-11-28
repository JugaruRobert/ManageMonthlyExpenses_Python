import datetime
import copy

#Verification

def verifyOption(x,test):
    """
    This function is used for verifying if the user has introduced a valid option in the
    openProgram module.
    Input: x - the string introduced by the user
    Output: True if the option is valid, False otherswise.
    """
    if len(x)!=1:
        if test==0:
            print("\nInvalid option.Please choose between 0,1 and 2.\n")
        return False
    elif x!="1" and x!="2" and x!="0":
        if test == 0:
            print("\nInvalid option.Please choose between 0,1 and 2.\n")
        return False
    return True

def invalidCommand():
    """
    This function is used for printing a message in the console
    (for an invalid command)
    input:-
    output:-
    """
    print("\nInvalid command.Please try again.\n\tType menu for help.\n")

def verifyAdd(a,categ,test):
    """
    This funcion validates the command - add -
    There are taken into consideration all the possible cases in which the command might be invalid.
    If the command is valid, a message is printed.
    input:a - the list of words in the command , categ - and array containing all the commands,
    test-an integer that shows if it's a test or not
    output: True if the command is valid, False otherwise
    """
    if len(a)!=3:
        if test==0:
            invalidCommand()
        return False
    elif a[1].isdigit()==False or int(a[1])<0:
        if test == 0:
            print("\nInvalid number.Please try again.\n\tChoose a natural number\n")
        return False
    elif a[2] not in categ:
        if test == 0:
            print("\nInvalid category.Please try again.\n\tChoose one of: transport,internet,housekeeping,food,clothes,others\n")
        return False
    return True

def verifyInsert(a,categ,test):
    """
    This funcion validates the command - insert -
    There are taken into consideration all the possible cases in which the command might be invalid.
    If the command is valid, a message is printed.
    input:a - the list of words in the command , categ - and array containing all the commands,
    test-an integer that shows if it's a test or not
    output: True if the command is valid, False otherwise
    """
    if len(a)!=4:
        if test == 0:
            invalidCommand()
        return False
    elif a[1].isdigit()==False:
        if test == 0:
            print("\nInvalid day.Please try again.\n\tChoose a number between 1 and 30 \n")
        return False
    elif a[2].isdigit()==False or int(a[2])<0:
        if test == 0:
            print("\nInvalid number.Please try again.\n\tChoose a natural number\n")
        return False
    elif int(a[1])<1 or int(a[1])>30:
        if test == 0:
            print("\nInvalid day.Please try again.\n\tChoose a number between 1 and 30 \n")
        return False
    elif a[3] not in categ:
        if test == 0:
            print("\nInvalid category.Please try again.\n\tChoose one of: transport,internet,housekeeping,food,clothes,others\n")
        return False
    return True

def verifyRemove(a,categ,test):
    """
    This funcion validates the command - remove -
    There are taken into consideration all the possible cases in which the command might be invalid.
    If the command is valid, a message is printed.
    input:a - the list of words in the command , categ - and array containing all the commands,
    test-an integer that shows if it's a test or not
    output: True if the command is valid, False otherwise
    """
    if len(a)==3 or len(a)==1 or len(a)==0 or len(a)>4:
        if test == 0:
            invalidCommand()
        return False
    elif len(a)==4:
        if a[2]!="to":
            if test == 0:
                invalidCommand()
            return False
        elif a[1].isdigit()==False or a[3].isdigit()==False:
            if test == 0:
                print("\nInvalid number.Please try again.\n\tChoose a natural number\n")
            return False

        elif (int(a[1])<1 or int(a[1])>30) or (int(a[3])<1 or int(a[3])>30):
            if test == 0:
                print("\nInvalid day.Please try again.\n\tChoose a number between 1 and 30 \n")
            return False

        elif int(a[3])<int(a[1]):
            if test == 0:
                print("\nInvalid command.Please try again.\n\tDay 2 must be greater than day 1 \n")
            return False

    elif a[1].isdigit()==False:
        if a[1] not in categ:
            if test == 0:
                invalidCommand()
            return False
    else:
        if int(a[1])<1 or int(a[1])>30:
            if test == 0:
                print("\nInvalid day.Please try again.\n\tChoose a number between 1 and 30 \n")
            return False
    return True

def verifyList(a,categ,test):
    """
    This funcion validates the command - list -
    There are taken into consideration all the possible cases in which the command might be invalid.
    If the command is valid, a message is printed.
    input:a - the list of words in the command , categ - and array containing all the commands,
    test-an integer that shows if it's a test or not
    output: True if the command is valid, False otherwise
    """
    sign=["<","=",">"]
    if len(a) !=1 and len(a)!=2 and len(a)!=4:
        if test == 0:
            invalidCommand()
        return False
    elif len(a)==2:
        if a[1].isdigit() == False:
            if a[1] not in categ:
                if test == 0:
                    invalidCommand()
                return False
        else:
            if int(a[1])<1 or int(a[1])>30:
                if test == 0:
                    print("\nInvalid day.Please try again.\n\tChoose a number between 1 and 30 \n")
                return False

    elif len(a)==4:
        if a[1] not in categ:
            if test == 0:
                print("\nInvalid category.Please try again.\n\tChoose one of: transport,internet,housekeeping,food,clothes,others\n")
            return False

        elif a[2] not in sign:
            if test == 0:
                invalidCommand()
            return False
        elif a[3].isdigit()==False:
            if test == 0:
                print("\nInvalid amount of money.Please try again.\n\tChoose a natural number \n")
            return False
    return True

def verifyFilter(a,categ,test):
    """
    This funcion validates the command - filter -
    There are taken into consideration all the possible cases in which the command might be invalid.
    If the command is valid, a message is printed.
    input:a - the list of words in the command , categ - and array containing all the commands,
    test-an integer that shows if it's a test or not
    output: True if the command is valid, False otherwise
    """
    sign=["<","=",">"]
    if len(a) !=2 and len(a)!=4:
        if test == 0:
            invalidCommand()
        return False
    elif len(a)==2:
        if a[1] not in categ:
            if test == 0:
                print("\nInvalid category.Please try again.\n\tChoose one of: transport,internet,housekeeping,food,clothes,others\n")
            return False

    else:
        if a[1] not in categ:
            if test == 0:
                print("\nInvalid category.Please try again.\n\tChoose one of: transport,internet,housekeeping,food,clothes,others\n")
            return False

        elif a[2] not in sign:
            if test == 0:
                invalidCommand()
            return False
        elif a[3].isdigit()==False:
            if test == 0:
                print("\nInvalid amount of money.Please try again.\n\tChoose a natural number \n")
            return False
    return True

def verifySum(a,categ,test):
    """
    This funcion validates the command - sum -
    There are taken into consideration all the possible cases in which the command might be invalid.
    If the command is valid, a message is printed.
    input:a - the list of words in the command , categ - and array containing all the commands,
    test-an integer that shows if it's a test or not
    output: True if the command is valid, False otherwise
    """
    if len(a)!=2:
        if test == 0:
            invalidCommand()
        return False
    elif a[1] not in categ:
        if test == 0:
            print("\nInvalid category.Please try again.\n\tChoose one of: transport,internet,housekeeping,food,clothes,others\n")
        return False
    return True

def verifyMax(a,test):
    """
    This funcion validates the command - max day -
    There are taken into consideration all the possible cases in which the command might be invalid.
    If the command is valid, a message is printed.
    input:a - the list of words in the command, test-an integer that shows if it's a test or not.
    output: True if the command is valid, False otherwise
    """
    if len(a)!=2:
        if test == 0:
            invalidCommand()
        return False
    elif a[1]!="day":
        if test == 0:
            invalidCommand()
        return False
    return True

def verifySort(a,categ,test):
    """
    This funcion validates the command - sort -
    There are taken into consideration all the possible cases in which the command might be invalid.
    If the command is valid, a message is printed.
    input:a - the list of words in the command , categ - and array containing all the commands,
    test-an integer that shows if it's a test or not
    output: True if the command is valid, False otherwise
    """
    if len(a)!=2:
        if test == 0:
            invalidCommand()
        return False
    elif a[1]!="day" and a[1] not in categ:
        if test == 0:
            invalidCommand()
        return False
    return True

def verifyCommand(a,categ,test):
    """
    This function validates all the commands.There are treated some particular
    cases in the beggining, such as: the command is not in the list of commands,
    or it is empty. Then , for every command it is called the function that
    verifies that specific command.
    If the command is valid, the changes are made,otherwise,a message is printed and the user must re-enter the command.
    input: a -the list of words in the command,categ-the list of categories,test-an integer that shows if it's a test or not.
    output: True if the command is valid, False otherwise
    """
    command=["add","insert","remove","menu","list","filter","help","sum","max","sort","undo","return","remove","exit"]

    if len(a)<1:
        if test == 0:
            invalidCommand()
        return False
    elif a[0] not in command:
        if test == 0:
            invalidCommand()
        return False
    else:
        if a[0]=="add":
            if verifyAdd(a,categ,0)==False:
                return False
            return True
        elif a[0]=="insert":
            if verifyInsert(a,categ,0)==False:
                return False
            return True
        elif a[0]=="remove":
            if verifyRemove(a,categ,0)==False:
                return False
            return True
        elif a[0]=="list":
            if verifyList(a,categ,0)==False:
                return False
            return True
        elif a[0]=="filter":
            if verifyFilter(a,categ,0)==False:
                return False
            return True
        elif a[0]=="list-all":
            if len(a)>1:
                if invalidCommand() == False:
                    return False
                return True
        elif a[0]=="sum":
            if verifySum(a,categ,0)==False:
                return False
            return True
        elif a[0]=="max":
            if verifyMax(a,0)==False:
                return False
            return True
        elif a[0]=="sort":
            if verifySort(a,categ,0)==False:
                return False
            return True
        elif a[0]=="menu" or a[0]=="exit" or a[0]=="help" or a[0]=="undo":
            if len(a)>1:
                if test == 0:
                    invalidCommand()
                return False
        elif a[0]=="return":
            if len(a)!=1:
                if test == 0:
                    invalidCommand()
                return False

    return True

#Execution

def executeCommand(d,a,categ,save):
    """
    This function is used for calling the specific execution function for every command.
    input:d-the dictionary,a-the list of the words in the command,categ-the array with categories,
    save-the list used for saving the dictionary for undo
    output:the dictionary
    """
    if a[0]=="insert":
        insertExpense(a[1],a[3],a[2],d,save,0)
    elif a[0]=="add":
        c=findCurrentDay()
        insertExpense(str(c),a[2],a[1],d,save,0)
    elif a[0]=="remove":
        if a[1] in categ:
            removeCategory(a[1],d,save,0)
        elif len(a)>2:
            removeMoreDays(a[1],a[3],d,save,0)
        else:
            removeDay(a[1],d,save,0)
    elif a[0] == "list":
        if len(a)==1:
            listAll(d, categ,0)
        elif len(a)==4:
            if a[2]=="<":
                listSmallerThan(d,int(a[3]),a[1],0)
            elif a[2]=="=":
                listEqual(d,int(a[3]),a[1],0)
            else:
                listGreaterThan(d,int(a[3]),a[1],0)
        elif a[1].isdigit() == True:
            list(d, a[1], categ,0)
        else:
            listCateg(d, a[1],0)
    elif a[0]=="sum":
        sum(d,a[1],0)
    elif a[0]=="max":
        maxDay(d,0)
    elif a[0]=="sort":
        if a[1] in categ:
            sortCateg(d,a[1],0)
        else:
            sortMonth(d,categ,0)
    elif a[0] == "filter":
        if len(a)==2:
            filterCateg(d,categ,a[1],save,0)
        else :
            if a[2] == "<":
                filterSmallerThan(d, int(a[3]), a[1],categ,save,0)
            elif a[2] == "=":
                filterEqual(d, int(a[3]), a[1],categ,save,0)
            else:
                filterGreaterThan(d, int(a[3]), a[1],categ,save,0)
    elif a[0]=="undo":
        d=undoCommand(d,save,0)
    return d

def findCurrentDay():
    """
    This function finds the current day from the computer,using the datetime library.
    input:-
    output: CurrentDay - integer number, the current day
    """
    CurrentDay=datetime.date.today()
    CurrentDay=CurrentDay.day
    return CurrentDay

def insertExpense(x,y,z,d,save,test):
    """
    This fuction is used for adding a (day-category-sum) triple to the dictionary.
    If the day exists, the sum of money it is added to the current sum in
    that category.
    input:x-the day, y-the category, z-the sum, d-the dictionary,test-an integer that shows if it's a test or not
    save-the list used for saving the dictionary for undo
    Output: the modified dictionary
    """
    c = copy.deepcopy(d)
    save.append(c)
    s=0
    if x in d :
        if y in d[x]:
            s=int(d[x][y])
            s=s+int(z)
            s=str(s)
            d[x][y]=s
        else:
            d[x][y]=z
    else:
        d[x]={y:z}
    if test==0:
        print("\n\tExpense added successfully")
    return d

def list(d,day,categ,test):
    """
    This function is used for listing all the expenses in a certain day.
    If the day it is in the dictionary,it is listed together with the
    categories and the sum for each category.
    Otherwise , a message is printed.
    input:d - the dictionary, day- the day that must pe printed,
    categ -the list of categories,test-an integer that shows if it's a test or not
    output: True if the day exists, False otherwise
    """
    if (day in d) and len(d[day])!=0 :
        if test == 0:
            print("\n Day",day,":")
            for j in categ:
                if j in d[day]:
                    print("\t",j,":",d[day][j],"RON")
    else:
        if test == 0:
            print("\n\tThere are no expenses in that day")
        return False
    return True

def listAll(d,categ,test):
    """
    This function is used for listing all the expenses in the dictionary.
    Every day that is in the dictionary is printed, together with the categories
    and the sum for each category.
    If the list is empty, a message is printed.
    The elements of the dictionary are printed in ascending order by day.
    input: d - the dictionary,categ - the list of categories,test - an integer that shows if it's a test or not
    output: True if there is at least one element in the dictionary, False otherwise
    """
    ok=False
    if len(d)==0:
        if test==0:
            print("\n\tThe list is empty")
        return False
    else:
        if test == 0:
            for i in range(1,31):
                i=str(i)
                if (i in d) and len(d[i])!=0 :
                    print("\n Day",i,":")
                    for j in categ:
                        if j in d[i]:
                            print("\t",j,":",d[i][j],"RON")
                            ok=True
        else:
            return True

    if ok==False:
        if test == 0:
            print("\n\tThe list is empty")
        return False
    return True

def listCateg(d,categ,test):
    """
    This function is used for listing all the expenses for a certain category.
    If the category is in the dictionary,it is listed together with the
    sum.Otherwise , a message is printed.
    input:d - the dictionary, categ - a certain category,test - an integer that shows if it's a test or not
    output: True if the category exists, False otherwise
    """
    ok=False
    if test==0:
        print("\n")
    for i in range(1,31):
        i=str(i)
        if i in d:
            if categ in d[i]:
                if test == 1:
                    return True
                print("Day",i,":",d[i][categ],"RON")
                ok=True

    if ok==False:
        if test == 0:
            print("\n\tThere are no expenses in that day")

    return False

def listSmallerThan(d,value,categ,test):
    """
    This function is used for listing the expenses that are smaller than a certain value.
    If the category is in the dictionary,it is printed the day that category is in
    together with the sum of money spent.
    Otherwise , a message is printed.
    input:d - the dictionary,value - an integer with the value,
    categ - a certain category,test - an integer that shows if it's a test or not
    output: True if the category exists, False otherwise
    """
    ok = False
    for i in range(1, 31):
        i = str(i)
        if i in d:
            if categ in d[i]:
                if int(d[i][categ]) < value:
                    if test == 1:
                        return True
                    if ok==False:
                        print("\nDay", i, ":", d[i][categ], "RON.")
                        ok = True
                    else:
                        print("Day", i, ":", d[i][categ], "RON.")

    if ok==False:
        if test == 0:
            print("\n\tThere are no expenses matching the command.")
    return False

def listEqual(d,value,categ,test):
    """
    This function is used for listing the expenses that are equal to a certain value.
    If the category is in the dictionary,it is printed the day that category is in
    together with the sum of money spent.
    Otherwise , a message is printed.
    input:d - the dictionary,value - an integer with the value,
    categ - a certain category,test - an integer that shows if it's a test or not
    output: True if the category exists, False otherwise
    """
    ok = False
    for i in range(1, 31):
        i = str(i)
        if i in d:
            if categ in d[i]:
                if int(d[i][categ]) == value:
                    if test == 1:
                        return True
                    if ok==False:
                        print("\nDay", i, ":", d[i][categ], "RON.")
                        ok = True
                    else:
                        print("Day", i, ":", d[i][categ], "RON.")
    if ok == False:
        if test == 0:
            print("\n\tThere are no expenses matching the command")

    return False

def listGreaterThan(d, value, categ,test):
    """
    This function is used for listing the expenses that are greater than a certain value.
    If the category is in the dictionary,it is printed the day that category is in
    together with the sum of money spent.
    Otherwise , a message is printed.
    input:d - the dictionary,value - an integer with the value,
    categ - a certain category,test - an integer that shows if it's a test or not
    output: True if the category exists, False otherwise
    """
    ok = False
    for i in range(1, 31):
        i = str(i)
        if i in d:
            if categ in d[i]:
                if int(d[i][categ]) > value:
                    if test == 1:
                        return True
                    if ok==False:
                        print("\nDay", i, ":", d[i][categ], "RON.")
                        ok = True
                    else:
                        print("Day", i, ":", d[i][categ], "RON.")
    if ok == False:
        if test == 0:
            print("\n\tThere are no expenses matching the command.")

    return False

def filterCateg(d, categList, categ, save,test):
    """
    This function is used for filtering all the expenses by only keeping in the
    dictionary expenses that are in a certain category.
    input:d - the dictionary,categ - a certain category, categList - a list with categories,
    test - an integer that shows if it's a test or not, save-the list used for saving the dictionary for undo
    output: True if the category exists, False otherwise
    """
    c = copy.deepcopy(d)
    save.append(c)
    ok = False
    for i in d:
        for x in categList:
            if (x in d[i]) and (x != categ):
                d[i].pop(x)
            ok = True

    for i in range(1,31):
        i=str(i)
        if i in d:
            if len(d[i])==0:
                d.pop(i)

    if ok == False:
        if test == 0:
            print("\n\tThere are no expenses in this category in the entire month.")
    else:
        if test == 0:
            print("\n\tFilter applied successufully.")
    return d

def filterSmallerThan(d, value, categ, categList, save,test):
    """
    This function is used for filtering all the expenses by only keeping in the dictionary
    expenses that are in a specific category  with the sum of money spent smaller than a specific value.
    input:d - the dictionary,categ- a certain category,value-an integer with the value
    categList -a list with categories,test-an integer that shows if it's a test or not
    save-the list used for saving the dictionary for undo.
    output: True if the category exists, False otherwise
    """
    c = copy.deepcopy(d)
    save.append(c)
    ok = False
    for i in d:
        for x in categList:
            if x in d[i]:
                if x != categ:
                    d[i].pop(x)
                    ok = True
                else:
                    ok = True
                    if int(d[i][categ]) > value:
                        d[i].pop(x)

    for i in range(1,31):
        i=str(i)
        if i in d:
            if len(d[i])==0:
                d.pop(i)

    if ok == False:
        if test == 0:
            print("\n\tThere are no expenses in this category in the entire month.")
    else:
        if test == 0:
            print("\n\tFilter applied successufully.")
    return d

def filterEqual(d, value, categ, categList, save,test):
    """
    This function is used for filtering all the expenses by only keeping in the dictionary
    expenses that are in a specific category  with the sum of money spent equal to a specific value.
    input:d - the dictionary,categ- a certain category,value-an integer with the value
    categList -a list with categories,test-an integer that shows if it's a test or not
    save-the list used for saving the dictionary for undo
    output: True if the category exists, False otherwise
    """
    c = copy.deepcopy(d)
    save.append(c)
    ok = False
    for i in d:
        for x in categList:
            if x in d[i]:
                if x != categ:
                    d[i].pop(x)
                    ok = True
                else:
                    ok = True
                    if int(d[i][categ]) != value:
                        d[i].pop(x)

    for i in range(1,31):
        i=str(i)
        if i in d:
            if len(d[i])==0:
                d.pop(i)

    if ok == False:
        if test == 0:
            print("\n\tThere are no expenses in this category in the entire month.")
    else:
        if test == 0:
            print("\n\tFilter applied successufully.")
    return d

def filterGreaterThan(d, value, categ, categList, save,test):
    """
    This function is used for filtering all the expenses by only keeping in the dictionary
    expenses that are in a specific category  with the sum of money spent greater than a specific value.
    input:d - the dictionary,categ- a certain category,value-an integer with the value
    categList -a list with categories,test-an integer that shows if it's a test or not
    save-the list used for saving the dictionary for undo
    output: True if the category exists, False otherwise
    """
    c = copy.deepcopy(d)
    save.append(c)
    ok = False
    for i in d:
        for x in categList:
            if x in d[i]:
                if x != categ:
                    d[i].pop(x)
                    ok = True
                else:
                    ok = True
                    if int(d[i][categ]) < value:
                        d[i].pop(x)

    for i in range(1,31):
        i=str(i)
        if i in d:
            if len(d[i])==0:
                d.pop(i)

    for i in range(1,31):
        i=str(i)
        if i in d:
            if len(d[i])==0:
                d.pop(i)

    if ok == False:
        if test == 0:
            print("\n\tThere are no expenses in this category in the entire month.")
    else:
        if test == 0:
            print("\n\tFilter applied successufully.")
    return d

def removeDay(x, d, save,test):
    """
    This function is used for removing a day from the dictionary
    If the day is found as a key in the dictionary,
    it is removed with the pop() command.Otherwise, a message is printed
    Input:x-the day that must be removed, d - the dictionary,test-an integer that shows if it's a test or not,
    save - the list used for saving the dictionary for undo
    Output: the modified dictionary
    """
    c = copy.deepcopy(d)
    save.append(c)
    if x in d:
        d.pop(x)
        if test==0:
            print("\n\tExpense deleted successfully.")
    else:
        if test == 0:
            print("\n\tThere are no expenses in this day.")
    return d

def removeMoreDays(day1, day2, d, save,test):
    """
    This function is used for removing a consecutive sequence of days from
    the dictionary.
    If any of the days is not found in the dictionary, a message is printed.
    Otherwise, the days are removed.
    Input: day1- the day from which the sequence starts,day2 - the day at which the sequence ends
    d - the dictionary,test - an integer that shows if it's a test or not
    save - the list used for saving the dictionary for undo
    Output: the modified dictionary
    """
    c = copy.deepcopy(d)
    save.append(c)
    ok = False
    day1 = int(day1)
    day2 = int(day2)
    for i in range(day1, day2 + 1):
        i = str(i)
        if i in d:
            d.pop(i)
            ok = True
    if ok == True:
        if test == 0:
            print("\n\tElement deleted successfully")
    else:
        if test == 0:
            print("\n\tNo expenses in any of these days")
    return d

def removeCategory(category, d, save,test):
    """
    This function is used for removing a category from the dictionary
    If the category is found as a in the dictionary ,
    it is removed with the pop() command.Otherwise, a message is printed
    Input:category-the category that must be removed, d - the dictionary,test-an integer that shows if it's a test or not
    save-the list used for saving the dictionary for undo
    Output: the modified dictionary
    """
    c = copy.deepcopy(d)
    save.append(c)
    ok = False
    for i in d:
        if category in d[i]:
            d[i].pop(category)
            ok = True
    if ok == True:
        if test == 0:
            print("\n\tElement deleted successufully")
    else:
        if test == 0:
            print("\n\tNo expenses in that category in any of the days")
    return d

def sum(d, categ,test):
    """
    This function is used for making the sum of the expenses from a certain category.
    Input:categ - a certain category, d - the dictionary,test - an integer that shows if it's a test or not
    Output:the modified dictionary
    """
    s = 0
    for i in d:
        if categ in d[i]:
            s = s + int(d[i][categ])
    if s == 0:
        if test==0:
            print("\n\tNo expenses in this category.")
        return False
    else:
        if test == 0:
            print("\nThe total amount of money spent on", categ, "is", s,"RON.")
    return True

def maxDay(d,test):
    """
    This function is used for printing the day that contains the maximum sum of expenses.
    Input:d - the dictionary,test-an integer that shows if it's a test or not
    Output: the modified dictionary
    """
    max = 0
    day = 0
    for i in d:
        s = 0
        for categ in d[i]:
            s = s + int(d[i][categ])
        if s > max:
            max = s
            day = int(i)
    if max != 0:
        if test == 0:
            print("\nThe day with the maximum amount of money spent is", day,".","Money spent:", max,"RON.")
        return True
    else:
        if test == 0:
            print("\n\tThe list of expenses is empty.")
        return False

def sortMonth(d, categ,test):
    """
    This function is used for sorting all the days in an ascending order by the total sum of expenses in that day.
    Input:categ - an array with categories, d - the dictionary,test - an integer that shows if it's a test or not.
    Output: the modified dictionary
    """
    b = []
    for i in d:
        s = 0
        for cat in d[i]:
            s = s + int(d[i][cat])
        b.append((s, i))

    if len(b) == 0:
        if test == 0:
            print("\n\tThe list is empty")
        return False

    b.sort()

    for i in range(0, len(b)):
        day = b[i][1]
        if day != 0:
            if test == 1:
                return True
            print("\n Day", day, ":")
            for j in categ:
                if j in d[day]:
                    print("\t", j, ":", d[day][j], "RON")
        print("\n\t\tTotal:", b[i][0], "RON")

def sortCateg(d,cat,test):
    """
    This function is used for sorting expenses in a certain category over the current month
    in ascending order by the sum of money spent.
    Input:cat - a certain category, d - the dictionary,test - an integer that shows if it's a test or not
    Output: the modified dictionary
    """
    b = []
    for i in d:
        if cat in d[i]:
            if test == 1:
                return True
            b.append((int(d[i][cat]), i))


    if len(b) == 0:
        if test == 0:
            print("\n\tThere are no expenses in this category.")
        return False

    b.sort()

    for i in range(0, len(b)):
        day = b[i][1]
        if day != 0:
            print("\n Day", day, ":")
            print("\t", cat, ":", b[i][0], "RON.")

def undoCommand(d, save,test):
    """
    This function is used for undoing the last made modification to the dictionary.
    With every modification, the dictionary is saved in the save array.
    In this function the dictionary will became what it was before the last modification.
    If there is no undo to be done, a message is printed.
    input:d-the dictionary,save- an array in which is memorated the dtcionary at every cange,
    test - an integer that shows if it's a test or not
    output: the dictionary
    """
    if len(save) == 0:
        if test==0:
            print("\n\tNothing left to undo.")
    else:
        d = copy.deepcopy(save[len(save) - 1])
        if test==0:
            print("\n\tUndo done.")
        save.pop()
    return d

def itemsForTest(d):
    """
    This function is used for adding some (day, category, sum of money) triple into the dictionary
    for testing purposes.
    input:d-the dictionary
    output:-the dictionary containing some elements
    """
    d["1"] = {"internet": "12", "food": "120"}
    d["2"] = {"housekeeping": "10000"}
    d["3"] = {"internet": "20", "clothes": "500"}
    d["6"] = {"internet": "15"}
    d["10"] = {"food": "45"}
    d["17"] = {"clothes": "420"}
    d["18"] = {"others": "520"}
    d["19"] = {"transport": "1160"}
    d["20"] = {"clothes": "100", "food": "300", "others": "10"}
    d["28"] = {"internet": "125", "food": "120", "others": "20", "clothes": "500", "transport": "1200",
               "housekeeping": "200"}
    return d

#  Tests ---------------------------------------------------------

def test(d,save):
    """
    This function calls all the other functions for tests
    input:d-the dictionary, save-the list used for saving the dictionary for undo
    output:the dictionary
    """

    categ = ["transport", "internet", "housekeeping", "others", "food", "clothes"]
    testVerifyOption()
    testVerifyAdd(categ)
    testVerifyInsert(categ)
    testVerifyRemove(categ)
    testVerifyList(categ)
    testVerifyFilter(categ)
    testVerifySum(categ)
    testVerifyMax()
    testVerifySort(categ)
    testVerifyCommand(categ)
    testInsertExpense(d,save)
    testRemoveDay(d, save)
    testRemoveMoreDays(d, save)
    testRemoveCategory(d, save)
    testList(d, save, categ)
    testListAll(categ,save)
    testListCateg(categ, save)
    testListSmallerThan(categ, save)
    testListGreaterThan(categ, save)
    testListEqual(categ, save)
    testSum(categ, save)
    testMaxDay(d,save)
    testSortMonth(d, categ, save)
    testSortCateg(d, save)
    testUndoCommand(d, save)
    testFilterCateg(d, categ, save)
    testFilterSmallerThan(d, categ, save)
    testFilterEqual(d, categ, save)
    testFilterGreaterThan(d, categ, save)
    return d

def testVerifyOption():
    """
    This function is used for testing purposes
    input: categ - an array with categories
    output:-
    """
    assert verifyOption("1",1) == True
    assert verifyOption("2",1) == True
    assert verifyOption("0",1) == True
    assert verifyOption("4",1) == False
    assert verifyOption("12",1) == False
    assert verifyOption("-2",1) == False

def testVerifyAdd(categ):
    """
    This function is used for testing purposes
    input: categ - an array with categories
    output:-
    """
    a=["add", "100", "food"]
    assert verifyAdd(a,categ,1) == True
    a = ["add", "10", "noCategory"]
    assert verifyAdd(a,categ,1) == False
    a = ["add", "food", "100"]
    assert verifyAdd(a,categ,1) == False
    a = ["add", "avc", "abc"]
    assert verifyAdd(a,categ,1) == False
    a = ["add", "avc", "abc","as"]
    assert verifyAdd(a, categ,1) == False

def testVerifyInsert(categ):
    """
    This function is used for testing purposes
    input: categ - an array with categories
    output:-
    """
    a=["insert","1", "100", "food"]
    assert verifyInsert(a,categ,1) == True
    a = ["insert","-1", "10", "food"]
    assert verifyInsert(a,categ,1) == False
    a = ["insert","40", "food", "100"]
    assert verifyInsert(a,categ,1) == False
    a = ["insert","1", "120", "noCategory"]
    assert verifyInsert(a,categ,1) == False
    a = ["insert","1", "abc", "internet"]
    assert verifyInsert(a,categ,1) == False
    a = ["insert","-12", "avc", "abc"]
    assert verifyInsert(a,categ,1) == False
    a = ["insert","-12", "avc", "abc","a"]
    assert verifyInsert(a,categ,1) == False

def testVerifyRemove(categ):
    """
    This function is used for testing purposes
    input: categ - an array with categories
    output:-
    """
    a = ["remove","12"]
    assert verifyRemove(a, categ,1) == True
    a = ["remove", "12","as"]
    assert verifyRemove(a, categ,1) == False
    a = ["remove", "-12"]
    assert verifyRemove(a, categ,1) == False
    a = ["remove", "40"]
    assert verifyRemove(a, categ,1) == False
    a = ["remove", "12","to","19"]
    assert verifyRemove(a, categ,1) == True
    a = ["remove", "19", "to", "10"]
    assert verifyRemove(a, categ,1) == False
    a = ["remove", "food"]
    assert verifyRemove(a, categ,1) == True
    a = ["remove", "noCategory"]
    assert verifyRemove(a, categ,1) == False

def testVerifyList(categ):
    """
    This function is used for testing purposes
    input: categ - an array with categories
    output:-
    """
    a = ["list", "12"]
    assert verifyList(a, categ, 1) == True
    a = ["list", "food"]
    assert verifyList(a, categ, 1) == True
    a = ["list", "food","<","100"]
    assert verifyList(a, categ, 1) == True
    a=["list"]
    assert verifyList(a, categ, 1) == True
    a = ["list", "-2"]
    assert verifyList(a, categ, 1) == False
    a = ["list", "40"]
    assert verifyList(a, categ, 1) == False
    a = ["list", "noCategory"]
    assert verifyList(a, categ, 1) == False
    a = ["list", "food","12"]
    assert verifyList(a, categ, 1) == False
    a = ["list", "food", "*", "100"]
    assert verifyList(a, categ, 1) == False
    a = ["list", "100", "<", "food"]
    assert verifyList(a, categ, 1) == False

def testVerifyFilter(categ):
    """
    This function is used for testing purposes
    input: categ - an array with categories
    output:-
    """
    a = ["filter", "12"]
    assert verifyFilter(a, categ, 1) == False
    a = ["filter", "food"]
    assert verifyFilter(a, categ, 1) == True
    a = ["filter", "asd"]
    assert verifyFilter(a, categ, 1) == False
    a = ["filter", "food","asd"]
    assert verifyFilter(a, categ, 1) == False
    a = ["filter", "food", "<","200"]
    assert verifyFilter(a, categ, 1) == True
    a = ["filter", "food", "=", "200"]
    assert verifyFilter(a, categ, 1) == True
    a = ["filter", "food", ">", "200"]
    assert verifyFilter(a, categ, 1) == True
    a = ["filter", "food", "<", "asd"]
    assert verifyFilter(a, categ, 1) == False
    a = ["filter", "asd", "=", "200"]
    assert verifyFilter(a, categ, 1) == False
    a = ["filter", "200", ">", "200"]
    assert verifyFilter(a, categ, 1) == False
    a = ["filter", "200", ">", "food"]
    assert verifyFilter(a, categ, 1) == False

def testVerifySum(categ):
    """
    This function is used for testing purposes
    input: categ - an array with categories
    output:-
    """
    a = ["sum", "12"]
    assert verifySum(a, categ, 1) == False
    a = ["sum", "12","food"]
    assert verifySum(a, categ, 1) == False
    a = ["sum"]
    assert verifySum(a, categ, 1) == False
    a = ["sum","asd"]
    assert verifySum(a, categ, 1) == False
    a = ["sum","food"]
    assert verifySum(a, categ, 1) == True

def testVerifyMax():
    """
    This function is used for testing purposes
    input: -
    output:-
    """
    a = ["max"]
    assert verifyMax(a,1) == False
    a = ["max","12"]
    assert verifyMax(a, 1) == False
    a = ["max", "food"]
    assert verifyMax(a, 1) == False
    a = ["max", "day","asd"]
    assert verifyMax(a, 1) == False
    a = ["max", "day"]
    assert verifyMax(a, 1) == True

def testVerifySort(categ):
    """
    This function is used for testing purposes
    input: categ - an array with categories
    output:-
    """
    a = ["sort"]
    assert verifySort(a,categ,1) == False
    a = ["sort","12"]
    assert verifySort(a, categ, 1) == False
    a = ["sort", "noCateg"]
    assert verifySort(a, categ, 1) == False
    a = ["sort", "food","asd"]
    assert verifySort(a, categ, 1) == False
    a = ["sort", "day", "asd"]
    assert verifySort(a, categ, 1) == False
    a = ["sort", "day"]
    assert verifySort(a, categ, 1) == True
    a = ["sort", "food"]
    assert verifySort(a, categ, 1) == True

def testVerifyCommand(categ):
    """
    This function is used for testing purposes
    input: categ - an array with categories
    output:-
    """
    a = ["noCategory"]
    assert verifyCommand(a, categ, 1) == False
    a = []
    assert verifyCommand(a, categ, 1) == False
    a = ["menu","asd"]
    assert verifyCommand(a, categ, 1) == False
    a = ["help", "asd"]
    assert verifyCommand(a, categ, 1) == False
    a = ["exit", "asd"]
    assert verifyCommand(a, categ, 1) == False
    a = ["menu"]
    assert verifyCommand(a, categ, 1) == True

#-----------------------------------------------------

def testInsertExpense(d,save):
    """
    This function is used for testing purposes
    input: d - the dictionary save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d = {}
    insertExpense("1","food","100",d,save,1)
    assert len(d) == 1
    insertExpense("2", "internet", "120", d, save,1)
    assert len(d) == 2
    insertExpense("10", "clothes", "2", d, save,1)
    assert len(d) == 3
    insertExpense("10", "clothes", "10", d, save,1)
    assert len(d) == 3
    insertExpense("1", "food", "100", d, save,1)
    assert len(d) == 3

def testRemoveDay(d,save):
    """
    This function is used for testing purposes
    input: d - the dictionary save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d = {}
    insertExpense("1","food","100",d,save,1)
    removeDay("1",d,save,1)
    assert len(d) == 0
    insertExpense("10", "clothes", "2", d, save,1)
    insertExpense("10", "clothes", "10", d, save,1)
    removeDay("10", d, save,1)
    assert len(d) == 0

def testRemoveMoreDays(d, save):
    """
    This function is used for testing purposes
    input: d - the dictionary save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d = {}
    insertExpense("1", "food", "100", d, save,1)
    removeMoreDays("1","2",d,save,1)
    assert len(d) == 0
    insertExpense("10", "clothes", "2", d, save,1)
    insertExpense("11", "clothes", "10", d, save,1)
    insertExpense("12", "clothes", "10", d, save,1)
    insertExpense("17", "clothes", "10", d, save,1)
    removeMoreDays("9", "20", d, save,1)
    assert len(d) == 0
    removeMoreDays("1", "20", d, save,1)
    assert len(d) == 0

def testRemoveCategory(d, save):
    """
    This function is used for testing purposes
    input: d - the dictionary save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d = {}
    insertExpense("1", "food", "100", d, save,1)
    removeCategory("food", d, save,1)
    for i in d:
        assert ("food" in d[i]) == False
    insertExpense("10", "clothes", "2", d, save,1)
    insertExpense("10", "clothes", "10", d, save,1)
    insertExpense("1", "clothes", "10", d, save,1)
    insertExpense("28", "clothes", "10", d, save,1)
    removeCategory("clothes", d, save,1)
    for i in d:
        assert ("food" in d[i]) == False

def testList(d,save,categ):
    """
    This function is used for testing purposes
    input: d - the dictionary save- an array used for saving the dictionary, for the undo command
    categ - an array with categories
    output:-
    """
    assert list(d,"1",categ,1)==False
    assert list(d, "12", categ,1) == False
    insertExpense("1", "food", "100", d, save,1)
    assert list(d, "1", categ,1) == True
    removeDay("1", d, save,1)
    assert list(d, "1", categ,1) == False

def testListAll(categ,save):
    """
    This function is used for testing purposes
    input: categ - an array with categories,save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d={}
    assert listAll(d, categ, 1) == False
    insertExpense("1", "food", "100", d, save, 1)
    assert listAll(d, categ, 1) == True

def testListCateg(categ,save):
    """
    This function is used for testing purposes
    input: categ - an array with categories,save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d = {}
    assert listCateg(d, categ, 1) == False
    insertExpense("1", "food", "100", d, save, 1)
    assert listCateg(d, "food", 1) == True

def testListSmallerThan(categ,save):
    """
    This function is used for testing purposes
    input: categ - an array with categories,save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d={}
    assert listSmallerThan(d,12,"food",1)==False
    insertExpense("1", "food", "100", d, save, 1)
    assert listSmallerThan(d, 120, "food", 1) == True
    assert listSmallerThan(d, 12, "food", 1) == False

def testListGreaterThan(categ,save):
    """
    This function is used for testing purposes
    input: categ - an array with categories,save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d={}
    assert listGreaterThan(d,12,"food",1)==False
    insertExpense("1", "food", "100", d, save, 1)
    assert listGreaterThan(d, 120, "food", 1) == False
    assert listGreaterThan(d, 10, "food", 1) == True

def testListEqual(categ,save):
    """
    This function is used for testing purposes
    input: categ - an array with categories,save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d={}
    assert listEqual(d,12,"food",1)==False
    insertExpense("1", "food", "100", d, save, 1)
    assert listEqual(d, 120, "food", 1) == False
    assert listEqual(d, 100, "food", 1) == True

def testSum(categ, save):
    """
    This function is used for testing purposes
    input: categ - an array with categories,save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d = {}
    assert sum(d, "food", 1) == False
    insertExpense("1", "food", "100", d, save, 1)
    assert sum(d, "food", 1) == True
    insertExpense("12", "food", "100", d, save, 1)
    assert sum(d, "food", 1) == True

def testMaxDay(d,save):
    """
    This function is used for testing purposes
    input: d - the dictionary, save- an array used for saving the dictionary, for the undo command
    output:-
    """
    d = {}
    assert maxDay(d,1) == False
    insertExpense("1", "food", "100", d, save, 1)
    assert maxDay(d, 1) == True
    insertExpense("2", "food", "100", d, save, 1)
    insertExpense("2", "food", "100", d, save, 1)
    assert maxDay(d, 1) == True

def testSortMonth(d, categ,save):
    """
    This function is used for testing purposes
    input: d - the dictionary,save- an array used for saving the dictionary, for the undo command
    categ - an array with categories.
    output:-
    """
    d = {}
    assert sortMonth(d,categ,1) == False
    insertExpense("1", "food", "100", d, save, 1)
    assert sortMonth(d, categ, 1) == True

def testSortCateg(d,save):
    """
    This function is used for testing purposes
    input: d - the dictionary, save- an array used for saving the dictionary, for the undo command
    categ - an array with categories
    output:-
    """
    d = {}
    assert sortCateg(d, "food", 1) == False
    insertExpense("1", "food", "100", d, save, 1)
    assert sortCateg(d, "internet", 1) == False
    assert sortCateg(d, "food", 1) == True

def testUndoCommand(d, save):
    """
    This function is used for testing purposes
    input: d - the dictionary, save- an array used for saving the dictionary, for the undo command
    categ - an array with categories
    output:-
    """
    d = {}
    undoCommand(d,save,1)
    assert len(d) == 0
    insertExpense("1", "food", "100", d, save, 1)
    insertExpense("10", "clothes", "2", d, save, 1)
    d=undoCommand(d, save, 1)
    assert len(d) == 1
    removeCategory("food", d, save, 1)
    d=undoCommand(d, save, 1)
    assert len(d) == 1
    d=undoCommand(d, save, 1)
    assert len(d) == 0

def testFilterCateg(d, categ,save):
    d = {}
    filterCateg(d,categ,"food",save,1)
    assert len(d) == 0
    insertExpense("10", "food", "2", d, save, 1)
    filterCateg(d, categ, "food", save, 1)
    assert len(d) == 1
    insertExpense("10", "food", "20", d, save, 1)
    filterCateg(d, categ, "food", save, 1)
    assert len(d) == 1
    insertExpense("10", "internet", "20", d, save, 1)
    filterCateg(d, categ, "food", save, 1)
    assert len(d) == 1
    insertExpense("10", "food", "20", d, save, 1)
    insertExpense("20", "food", "20", d, save, 1)
    insertExpense("11", "clothes", "20", d, save, 1)
    insertExpense("2", "others", "20", d, save, 1)
    filterCateg(d, categ, "food", save, 1)
    assert len(d) == 2

def testFilterSmallerThan(d,categ,save):
    """
    This function is used for testing purposes
    input: d - the dictionary,save- an array used for saving the dictionary, for the undo command
    categ - an array with categories.
    output:-
    """
    d = {}
    filterSmallerThan(d, 12 , "food",categ, save, 1)
    assert len(d) == 0
    insertExpense("10", "food", "20", d, save, 1)
    filterSmallerThan(d, 12, "food", categ, save, 1)
    assert len(d) == 0
    insertExpense("10", "food", "2", d, save, 1)
    filterSmallerThan(d, 30, "food", categ, save, 1)
    assert len(d) == 1
    insertExpense("10", "food", "20", d, save, 1)
    insertExpense("11", "internet", "20", d, save, 1)
    insertExpense("12", "food", "60", d, save, 1)
    filterSmallerThan(d, 50, "food", categ, save, 1)
    assert len(d) == 1

def testFilterEqual(d,categ,save):
    """
    This function is used for testing purposes
    input: d - the dictionary,save- an array used for saving the dictionary, for the undo command
    categ - an array with categories.
    output:-
    """
    d = {}
    filterEqual(d, 12 , "food",categ, save, 1)
    assert len(d) == 0
    insertExpense("10", "food", "20", d, save, 1)
    filterEqual(d, 12, "food", categ, save, 1)
    assert len(d) == 0
    insertExpense("10", "food", "2", d, save, 1)
    filterEqual(d, 2, "food", categ, save, 1)
    assert len(d) == 1
    insertExpense("10", "food", "20", d, save, 1)
    insertExpense("11", "internet", "20", d, save, 1)
    insertExpense("12", "food", "60", d, save, 1)
    filterEqual(d, 22, "food", categ, save, 1)
    assert len(d) == 1

def testFilterGreaterThan(d,categ,save):
    """
    This function is used for testing purposes
    input: d - the dictionary,save- an array used for saving the dictionary, for the undo command
    categ - an array with categories.
    output:-
    """
    d = {}
    filterGreaterThan(d, 12 , "food",categ, save, 1)
    assert len(d) == 0
    insertExpense("10", "food", "20", d, save, 1)
    filterGreaterThan(d, 25, "food", categ, save, 1)
    assert len(d) == 0
    insertExpense("10", "food", "2", d, save, 1)
    filterGreaterThan(d, 10, "food", categ, save, 1)
    #assert len(d) == 1
    insertExpense("10", "food", "20", d, save, 1)
    insertExpense("11", "internet", "20", d, save, 1)
    insertExpense("12", "food", "15", d, save, 1)
    filterGreaterThan(d, 18, "food", categ, save, 1)
    assert len(d) == 1

