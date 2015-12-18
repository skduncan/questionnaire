#Authors: Colin Chandler and Sam Duncan
#Language: Questionnaire

from sys import *
import re

tokenList = []
variables = {}

def openFile(file):
    return open(file, "r").read() +  " <EOF>"

def lexer(contents):
    pattern1 = re.compile("\"(.*)")
    pattern2 = re.compile("\"(.*)\"")
    file = contents.split()
    i = 0
    while i < len(file):
        token = file[i]
        b = re.match(pattern1, token)

        if token == "<EOF>":
            tokenList.append(token)
            break

        elif token == "saywhat":
            tokenList.append("PRINT")

        elif b:
            n = 0
            x = i
            while n != 1:
                d = re.match(pattern2, token)
                x += 1
                if d:
                    tokenList.append("STRING" + token)
                    n = 1
                else:
                    token += " " + file[x]
        elif token.isnumeric():
            tokenList.append("NUM" + token)
        elif file[i] == "+" or file[i] == "-" or file[i] == "*" or file[i] == "/" or file[i] == "%":
            tokenList.append(token)
        elif token.lower() == "its":
            tokenList.append("EQUALS")
        elif token.lower() == "itsits":
            tokenList.append("EQEQ")
        elif token.lower() == "maybe":
            tokenList.append("IF")
        elif token == "?":
            tokenList.append("THEN")
        elif token == "!":
            tokenList.append("ENDIF")
        elif token.lower() == "whatis":
            tokenList.append("VAR")
            tokenList.append(file[i+1])
            i += 1
        i += 1
        token = ""
    return tokenList

def parse(toks):
    i = 0
    while(i < len(toks)):
        # VAR X =
        if toks[i] == "VAR" and toks[i+2] == "EQUALS":
            #VAR X = NUM ~
            if toks[i+3][0:3] == "NUM":
                #VAR X = NUM + ~
                if toks[i+4] == "+" or toks[i+4] == "-" or toks[i+4] == "*" or toks[i+4] == "/" or toks[i+4] == "%":
                    # VAR X = NUM + NUM
                    if toks[i+5][0:3] == "NUM":
                        variables[toks[i+1]] = str(eval(toks[i+3][3:] + toks[i+4] + toks[i+5][3:]))
                        i += 5
                        #VAR X = NUM + VAR Y
                    elif toks[i+5] == "VAR":
                        var3 = variables[toks[i+6]]
                        variables[i+1] = str(eval(toks[i+3][3:] + toks[i+4] + var3))
                        i += 6
                #VAR X = NUM
                else:
                    variables[toks[i+1]] = toks[i+3][3:]
                    i += 3
                #VAR X = VAR Y ~
            elif toks[i+3] == "VAR":
                var1 = variables[toks[i+4]]
                #VAR X = VAR Y +
                if toks[i+5] == "+" or toks[i+5] == "-" or toks[i+5] == "*" or toks[i+5] == "/" or toks[i+5] == "%":
                    #VAR X = VAR Y + VAR Z
                    if toks[i+6] == "VAR":
                        var2 = variables[toks[i+7]]
                        variables[i+1] = str(eval(var1 + toks[i+5] + var2))
                        i += 7
                        #VAR X = VAR Y + NUM
                    elif toks[i+6][0:3] == "NUM":
                        variables[toks[i+1]] = str(eval(var1 + toks[i+5] + toks[i+6][3:]))
                        i += 6
                else:
                    variables[toks[i+1]] = var1
                    i += 4
            else:
                variables[toks[i+1]] = toks[i+3][6:]
                i += 3
        if toks[i] == "PRINT":
            if toks[i+1][0:6] == "STRING":
                print(toks[i+1][6:])
                i += 1
            elif toks[i+1] == "VAR":
                print(variables[toks[i+2]])
                i += 2
            elif toks[i+1][0:3] == "NUM":
                if toks[i+2] == "+" or toks[i+2] == "-" or toks[i+2] == "*" or toks[i+2] == "/" or toks[i+2] == "%":
                    print(str(eval(toks[i+1][3:] + toks[i+2] + toks[i+3][3:])))
                    i += 3
                else:
                    print(toks[i+1][3:])
        if toks[i] == "IF":
            if toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "IF NUM EQEQ NUM THEN":
                if toks[i+1][3:] != toks[i+3][3:]:
                    j = i + 4
                    while toks[j] != "ENDIF":
                        j += 1
                    i = j
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3] + " " + toks[i+5] == "IF NUM EQEQ VAR THEN":
                numVar = variables[toks[i+4]]
                if toks[i+1][3:] != numVar:
                    j = i + 5
                    while toks[j] != "ENDIF":
                        j += 1
                    i = j
            elif toks[i] + " " + toks[i+1] + " " + toks[i+3] + " " + toks[i+4][0:3] + " " + toks[i+5] == "IF VAR EQEQ NUM THEN":
                varNum = variables[toks[i+2]]
                if varNum != toks[i+4][3:]:
                    j = i + 5
                    while toks[j] != "ENDIF":
                        j += 1
                    i = j
            elif toks[i] + " " + toks[i+1] + " " + toks[i+3] + " " + toks[i+4] + " " + toks[i+6] == "IF VAR EQEQ VAR THEN":
                var1 = variables[toks[i+2]]
                var2 = variables[toks[i+5]]
                if var1 != var2:
                    j = i + 6
                    while toks[j] != "ENDIF":
                        j+=1
                    i = j
        i += 1

def run():
    data = openFile(argv[1])
    tokens = lexer(data)
    parse(tokens)

run()
