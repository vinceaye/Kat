import random
import re
#class has modifier or not
#floofyblackones(public) purrivate(private) britishshorthair(protected) depawult(no access modifier)

#variables biscuits(number) yarn(string) boolean
#Gimme 5 biscuits in a bag! (bag = 5)
#Gimme "String" in a bag! (bag = "String")
#It gotta be true! (It = True)

#main is "scratcher" (is needed)

#no syntax errors, only words of affirmation

#if (purr) if-else (purrs if) else (hiss)

#loops are goto statements, pounce label

#print is "meow" (Meow "string")

#eeps indicates end of program

#new code within the class must be indented by 4 spaces
#new code within a function must be indented by 4 more spaces

#mice = label for goto

#CURRENT ISSUE IS IF STATEMENTS CANT WORK IN GOTOS

vars = dict()
classes = dict()
whitespaceList = []
ifBodyList = []

def assignStatement(state, expression, datatype):
    return 0

def errorMessage():
        errorsList = {"Error. Keep going, programmer! Your dedication and effort are paving the way for success. You're doing an amazing job!", 
                      "Error. Don't give up, coder! Every line of code you write is a step forward. Your perseverance is commendable, and you're making great progress!", 
                      "Error. You've got this, developer! Your commitment to learning and problem-solving is truly inspiring. Keep pushing through!",
                      "Error. Hang in there, programmer! Your passion for coding shines through in your work. Embrace the journey, stay focused, and trust in your abilities.",
                      "Error. You're doing fantastic, coder! Your skills are growing with each project you tackle. Stay confident, stay motivated, and keep up the amazing work!"}
        print(random.choice(list(errorsList)))

def varmap(targetVar, state):
    if targetVar in state:
        return state[targetVar]
    else:
        raise ValueError("Error: Var not found")

def isModifier(modifier):
    if (modifier == "floofyblackones" or modifier == "purrivate" or modifier == "britishshorthair" or modifier == "depawult"):
        return True
    else:
        return False

def isDataType(datatype):
    #note that the "void" datatype is exclusive to method signatures
    if (datatype == "biscuits" or datatype == "yarn" or datatype == "boolean" or datatype == "void"):
        return True
    else:
        return False

def count_whitespaces(line):
        count = 0
        for char in line:
            if char.isspace():
                count += 1
            else:
                break
        return count

#print statement called when "Meow" is found
def printStatement(line):
    match = re.search(r'"([^"]*)"', line)
    if match:
        string = match.group(1)
        print(string)
    else:
        try:
            #prints value of variable
            var = line.split()[1]
            val = varmap(var, vars)
            print(val)
        except:
            errorMessage()

def assignStatement(state,expression, line, datatype):
    match (datatype):
        case "biscuits":
            var = line.split()[len(line.split())-1]
            var = var[:-1]
            if (var.isidentifier() == False):
                errorMessage()
                return
            val = expression
            vars[var] = (int)(val)
            return state
        case "yarn":
            var = line.split()[len(line.split())-1]
            var = var[:-1]
            val = expression
            if (var.isidentifier() == False):
                errorMessage()
                return
            vars[var] = val
            return state
        case "boolean":
            var = line.split()[0]
            if (var.isidentifier() == False):
                errorMessage()
                return
            val = line.split()[len(line.split())-1]
            val = val[:-1]
            
            if (val == "True"):
                vars[var] = True
            elif (val == "False"):
                vars[var] = False
            else:
                errorMessage()
                return
            return state
        
def computeStatement(state,expression):
    expression = expression.strip()
    var,expression = expression.split("eets")
    operators = ['+','-','*','/','%']
    for operator in operators:
        if operator in expression:
        #Operator found in expression
            operation = eval(expression,state)
            vars[var.strip()] = operation
            return state
    else:
        #No operator found in expression
        errorMessage()
    return state
        
def ifElifElseStatement(state,line):
    #Regex to find boolean
    evalResult = False
    pattern = r'\((.*?)\)'
    match = re.findall(pattern, line.strip())
    if match:
        evalResult = eval(match[0], state)
    return evalResult

def ifBody(vars, line):
    keyword = line.split()
    if (keyword[0] == "Meow"):
        # Get the string inside the quotes
        printStatement(line)
        #"Gimme" is a keyword for variable declaration    
    elif (keyword[0] == "Gimme"):
        #regex to find string literals for variable assignment of type "yarn"
        match = re.search(r'"([^"]*)"', line)
        if match:
            string = match.group(1)
            assignStatement(vars, string, line, "yarn")
        else:
            #regex to find integers for variable assignment of type "biscuits"
            match = re.findall(r'\b\d+\b|\bbiscuits\b', line)
            if match:
                numbers = [int(num) for num in match if num.isdigit()]
                assignStatement(vars, numbers[0], line, "biscuits")
            else:
                errorMessage()              
    elif (keyword[1] == "gotta"):
            assignStatement(vars,"", line, "boolean")
            #math expression
    elif (keyword[1] == "eets"):
            computeStatement(vars, line)
    elif (keyword[0] == "purr") and (checkOthers == False):
                evaluateIf = ifElifElseStatement(vars, line)
                if (evaluateIf == True):
                    checkOthers = False
    elif (keyword[0] == "purrsif") and (checkOthers == False):
                evaluateIf = ifElifElseStatement(vars, line)
                if (evaluateIf == True):
                    checkOthers = False
    elif (keyword[0] == "hiss") and (checkOthers == False):
                evaluateIf = True
                if (evaluateIf == True):
                    checkOthers = False
checkOthersGoto = dict()
checkOthersGoto["called"] = False
def ifBodyGoto(vars, line, checkOtherso):
    keyword = line.split()
    if (keyword[0] == "Meow"):
        # Get the string inside the quotes
        printStatement(line)
        #"Gimme" is a keyword for variable declaration    
    elif (keyword[0] == "Gimme"):
        #regex to find string literals for variable assignment of type "yarn"
        match = re.search(r'"([^"]*)"', line)
        if match:
            string = match.group(1)
            assignStatement(vars, string, line, "yarn")
        else:
            #regex to find integers for variable assignment of type "biscuits"
            match = re.findall(r'\b\d+\b|\bbiscuits\b', line)
            if match:
                numbers = [int(num) for num in match if num.isdigit()]
                assignStatement(vars, numbers[0], line, "biscuits")
            else:
                errorMessage()              
    elif (len(keyword) > 1) and (keyword[1] == "gotta"):
        assignStatement(vars,"", line, "boolean")
        #math expression
    elif (len(keyword) > 1) and (keyword[1] == "eets"):
        computeStatement(vars, line)
    elif (keyword[0] == "purr") and (checkOthers == False):
                evaluateIf = ifElifElseStatement(vars, line)
                if (evaluateIf == True):
                    checkOthers = True
                    
    elif (keyword[0] == "purrsif") and (checkOthers == False):
                evaluateIf = ifElifElseStatement(vars, line)
                if (evaluateIf == True):
                    checkOthers= True
                    
    elif (keyword[0] == "hiss") and (checkOthers == False):
                evaluateIf = True
                if (evaluateIf == True):
                    checkOthers = True
                    

def gotoStatement(vars, gotoBody):
    checkOthers = True
    evaluateIf = False
    for line in gotoBody:
        keyword = line.split()
        if (keyword[0] == "purr"):
            #finds condition in line and evaluates it
            evaluateIf = ifElifElseStatement(vars, line)
            if (evaluateIf):
                checkOthers = False
                i = 0
                #saves if body into a list
                while (gotoBody[i].strip() != ">.<"):
                    ifBodyList.append(gotoBody[i])
                    i += 1
                #evaluates the if body
        i = 0
        while (i < len(ifBodyList)) and (checkOthersGoto["called"] == True):
            ifBodyGoto(vars, ifBodyList[i],checkOthersGoto)
            i += 1
            continue 

        if (count_whitespaces(line) == 16) or (keyword[0] == "purr") or (keyword[0] == "purrsif") or (keyword[0] == "hiss"):
            continue

        if (keyword[0] == "Meow"):
            # Get the string inside the quotes
            printStatement(line)
        #"Gimme" is a keyword for variable declaration    
        elif (keyword[0] == "Gimme"):
            #regex to find string literals for variable assignment of type "yarn"
            match = re.search(r'"([^"]*)"', line)
            if match:
                string = match.group(1)
                assignStatement(vars, string, line, "yarn")
            else:
                #regex to find integers for variable assignment of type "biscuits"
                match = re.findall(r'\b\d+\b|\bbiscuits\b', line)
                if match:
                    numbers = [int(num) for num in match if num.isdigit()]
                    assignStatement(vars, numbers[0], line, "biscuits")
                else:
                    errorMessage()              
        elif (len(keyword) > 1) and (keyword[1] == "gotta"):
            assignStatement(vars,"", line, "boolean")
            #math expression
        elif (len(keyword) > 1) and (keyword[1] == "eets"):
            computeStatement(vars, line)
       

def read_file(file_name):
    with open(file_name, 'r') as file:
        classList = []
        linenum = 0
        #whether a class has a scratcher function or not
        hasScratcher = False
        #variable to check if the current code is in a method
        inMethod = False
        evaluateIf = False
        #variable to check if the current if statement is false, if so, do not check the other if/elif/else statements
        checkOthers = True
        routeTaken = False
        #variable to save goto body and check if label is valid
        gotoBody = []
        isGoto = False
        #structure of the indentations
        classWhiteSpaces = 0
        functionWhiteSpaces = 4
        functionBodyWhiteSpaces = 8

        
        for line in file:
            if (line.strip() == "eeps"):
                 return
            #mew is the keyword for the end of an if statement, so if reached then evaluate the if body
            if (line.strip() == "mew") and (routeTaken):
                i = 0
                while i < len(ifBodyList):
                    ifBody(vars, ifBodyList[i])
                    i += 1
                evaluateIf = False
                checkOthers = False
                routeTaken = False
                ifBodyList.clear()
                continue
            
            #">.<" is the keyword for the end of a series of if/elif/else statements
            if (line.strip() == ">.<"):
                checkOthers = True
            
            #analyzes the goto statement and its body
            if ("pounce on" in line) and (count_whitespaces(line) == functionBodyWhiteSpaces):
                if line.strip().split()[2] != "mice":
                    #the keyword mice should be in the goto statement
                    errorMessage()
                    return
                match = re.search(r'\((.*?)\)', line)
                if match:
                    conditional_statement = match.group(1)
                    boolResult = eval(conditional_statement, vars)
                    while(boolResult):
                        gotoStatement(vars, gotoBody)
                        boolResult = eval(conditional_statement, vars)
                    isGoto = False
                else:
                    errorMessage()
                    return
                    

            #makes sure that all of the if body is executed before moving on to code outside the if statement
            # if ((evaluateIf == False) and len(ifBodyList) > 0):
            #     if (whitespaceList[0] == count_whitespaces(line)):
            #         evaluateIf = False   
            #     i = 0
                
            #     checkOthers = True
            #     ifBodyList.clear() 

            #must check line for class declaration
            #class declaration must have: 
            #3 keywords: modifier, datatype, classname
            #a colon at the end
            #no whitespaces in the beginning
           
            if (count_whitespaces(line) == classWhiteSpaces):
                keywords = line.split()
                if (len(keywords) != 3):
                    #if error in class declaration, print error message
                    errorMessage()
                    return
                modifier, datatype, classname = keywords
                if (classname[len(classname)-1] != ":"):
                    #missing colon, so error in class declaration
                    errorMessage()
                    return
                #throws an error if any of the class declaration is wrong
                if ((isModifier(modifier) == False) or (datatype != "class") or (classname[:-1].isidentifier() == False)):
                    errorMessage()
                    return
                

            #if there are 4 whitespaces, then it is a function declaration, first one should be "scratcher"
            #CURRENT ISSUE, IF SCRATCHER ISNT FIRST THEN PROGRAM WILL CAUSE ERROR, FIX LATER, TRY TO ADD METHOD CALLS    
            elif (count_whitespaces(line) == functionWhiteSpaces) and (hasScratcher == False):
                keywords = line.split()
                modifier, returnType, funcName = keywords
                if (len(keywords) != 3):
                    #if error in function declaration, print error message
                    errorMessage()
                    return
                #if this is not the main aka "scratcher" method, print error message
                if (funcName[:-3] != "scratcher"):
                    
                    errorMessage()
                    return
                #main method must be void, else print error message
                if (returnType != "void"):
                    errorMessage()
                    return
                if ((isModifier(modifier) == False) or (isDataType(returnType) == False) or (classname[:-1].isidentifier() == False)):
                    errorMessage()
                    return
                hasScratcher = True
                inMethod = True
                
            
            #Any method not the main method    
            elif (count_whitespaces(line) == functionWhiteSpaces) and (hasScratcher == True):
                keywords = line.split()
                modifier, returnType, funcName = keywords
                print(modifier, returnType, funcName[:-3])
                if (len(keywords) != 3):
                    #if error in function declaration, print error message
                    errorMessage()
                    return
                #cannot have more than one scratcher method
                if (funcName[:-3] == "scratcher"):
                    errorMessage()
                    return
                #method must have valid return type, else print error message
                if (isDataType(returnType) == False):
                    errorMessage()
                    return
                if ((isModifier(modifier) == False) or (isDataType(returnType) == False) or (classname[:-1].isidentifier() == False)):
                    errorMessage()
                    return
                hasScratcher = True
                inMethod = True

            
                
            #analyzing code inside the method
            elif (count_whitespaces(line) == functionBodyWhiteSpaces) and (hasScratcher == True) and (inMethod == True) and (evaluateIf == False) and (line.strip() != "endMeowthod"):
        
                functionBodyWhiteSpaces = count_whitespaces(line)
                whitespaceList.append(functionBodyWhiteSpaces)
                #makes sure those inside if statements arent executed here
                if (count_whitespaces(line) != whitespaceList[0]):
                    checkOthers = True
                    continue
                # Get the first element of the line
                evaluateIf = False
                keyword = line.split()
                if (keyword[0] == "Meow"):
                    # Get the string inside the quotes
                    printStatement(line)
                #"Gimme" is a keyword for variable declaration    
                elif (keyword[0] == "Gimme"):
                    #regex to find string literals for variable assignment of type "yarn"
                    match = re.search(r'"([^"]*)"', line)
                    if match:
                        string = match.group(1)
                        assignStatement(vars, string, line, "yarn")
                    else:
                        #regex to find integers for variable assignment of type "biscuits"
                        match = re.findall(r'\b\d+\b|\bbiscuits\b', line)
                        if match:
                            numbers = [int(num) for num in match if num.isdigit()]
                            assignStatement(vars, numbers[0], line, "biscuits")
                        else:
                            errorMessage()
                #boolean assignment
                elif (len(keyword) > 1) and (keyword[1] == "gotta"):
                    assignStatement(vars,"", line, "boolean")
                #math expression
                elif (len(keyword) > 1) and (keyword[1] == "eets"):
                    computeStatement(vars, line)
                #if checkOthers is true, it means that the current if statement is false, so check the other if/elif/else statements
                elif (keyword[0] == "purr") and (checkOthers == True) and (routeTaken == False):
                    evaluateIf = ifElifElseStatement(vars, line)
                    if (evaluateIf == True):
                        checkOthers = False
                        routeTaken = True
                    continue
                elif (keyword[0] == "purrsif") and (checkOthers == True) and (routeTaken == False):
                    evaluateIf = ifElifElseStatement(vars, line)
                    if (evaluateIf == True):
                        checkOthers = False
                        routeTaken = True
                    continue
                elif (keyword[0] == "hiss") and (checkOthers == True) and (routeTaken == False):
                    evaluateIf = True
                    checkOthers = False
                    routeTaken = True
                    continue
                elif (keyword[0] == "mice"):
                    isGoto = True
                    continue

                
                
            #same as code above but for analyzing the body of an if statement
            elif (count_whitespaces(line) > functionBodyWhiteSpaces) and (hasScratcher == True) and (inMethod == True) and (evaluateIf == True) and (line.strip() != "endMeowthod"):
                ifBodyList.append(line)
                continue

            elif (isGoto == True) and (count_whitespaces(line) > functionBodyWhiteSpaces):
                gotoBody.append(line)
                continue
                

            #end of method is reached
            elif (line == "endMeowthod"):
                inMethod = False
                continue
                

            #saves class name and the lines of code inside it in a dictionary
            
        # print(classes) 
                
    
    

    # # Example usage:
    # line = "          This is a line with some whitespaces"
    # whitespace_count = count_whitespaces(line)
    # print(f"The line has {whitespace_count} whitespaces.")
    


read_file("prog3.kat")