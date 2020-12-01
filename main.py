from node import *
from collections import deque

nonterminals = list()
terminals = list()
initial = ""
productions_dict = dict()

def SelectFile():
    """
    docstring
    """
    filename = input("Please enter the name of the file you want to work with (include '.txt') : ")
    ReadFile(filename)

def ReadFile(filename):
    """
    docstring
    """
    global nonterminals
    global terminals
    global initial
    global productions_dict

    with open(filename) as f_obj:
        lines = f_obj.read().splitlines()

    nonterminals = lines[0].split(",")
    terminals = lines[1].split(",")
    initial = lines[2]

    for x in range(3, len(lines)):
        temp1 = lines[x].split("->")
        print(temp1)
        productions_dict[x-2] = temp1
    PrintGrammar()
    #Menu()

def PrintGrammar():
    """
    docstring
    """
    print()
    print("Non-terminal symbols: ", end="")
    for symbol in nonterminals:
        print(symbol, end=" ")
    print()
    print("Terminal symbols: ", end="")
    for symbol in terminals:
        print(symbol, end=" ")
    print()
    print("Start symbol: ", end="")
    print(initial)
    for key in productions_dict:
        print("Production: " + productions_dict[key][0] + "->" + productions_dict[key][1])
    Menu()

def Menu():
    """
    docstring
    """
    print()
    print("------------------------------------")
    test_input = input("Please enter the string to be tested: ")
    max_depth = int(input("Please enter the maximum depth: "))
    print("------------------------------------")
    print()

    root = BuildTree(test_input, max_depth)
    GenerateSyntax(root)


def BuildTree(test_input, max_depth):
    """
    docstring
    """
    root = Node(initial)
    q = deque()
    q.append(root)
    uwv = ""
    actualdepth = 0

    while q and test_input != uwv and actualdepth <= max_depth:
        tempNode = q.popleft()
        i = 0
        done = False
        varsust = GetLeft(tempNode)

        while done == False and test_input != uwv:
            val = FindProductions(varsust, i)
            if  val == -1:
                done = True
            else:
                j = val
                vartemp = productions_dict[j][1]
                uwv = tempNode.data.replace(varsust, vartemp, 1)
                temp = Node(uwv)
                tempNode.AddChild(temp)

                if EnterQueue(uwv, test_input):
                    q.append(temp)
                i = j
                actualdepth = temp.CalculateDepth()
                if actualdepth > max_depth:
                    temp.DeleteNode()
    if test_input == uwv and actualdepth <= max_depth:
        print("Input: " + test_input + " was accepted and found in level: " + str(actualdepth+1) + " with depth: " + str(actualdepth))
    else:
        print("Input: " + test_input + " was not accepted")
    print()
    return root


def GetLeft(tempNode):
    """
    docstring
    """
    for i in range(0, len(tempNode.data)):
        for nonterminal in nonterminals:
            if tempNode.data[i] == nonterminal:
                return nonterminal
    return None

def FindProductions(varsust, i):
    """
    docstring
    """
    for x in range(i+1, len(productions_dict)+1):
        if productions_dict[x][0] == varsust:
            return x
    return -1

def EnterQueue(uwv, test_input):
    """
    docstring
    """
    for symbol in nonterminals:
        if uwv[0] == symbol:
            return True
    uwvtrimmed = ""
    index = 0
    found = False

    for i in range(0, len(uwv)):
        for symbol in nonterminals:
            if uwv[i] == symbol and found == False:
                index = i
                found = True
    uwvtrimmed = uwv[0:index]

    if len(uwvtrimmed) > len(test_input):
        return False
    else:
        for w in range(0, len(uwvtrimmed)):
            if uwvtrimmed[w] != test_input[w]:
                return False
        return True

def GenerateSyntax(root):
    """
    docstring
    """
    result = ""
    stack = deque()
    stack.append(root)

    while stack:
        nodeTemp = stack.pop()
        result += "[" + nodeTemp.data

        if len(nodeTemp.son) == 0:
            nodeTemp.EditRemaining(0)
            if nodeTemp.parent == None:
                result += "]"
            else:
                if nodeTemp.remaining == 0:
                    result += "]"
                papa = nodeTemp.parent
                papa.EditRemaining(papa.remaining-1)
                while nodeTemp.parent != None and nodeTemp.parent.remaining == 0:
                    nodeTemp = nodeTemp.parent
                    if nodeTemp.remaining == 0 and nodeTemp.deuda == False:
                        result += "]"
                        nodeTemp.EditDeuda(True)
        else:
            if len(nodeTemp.son) != 0:
                if nodeTemp.parent != None:
                    papa = nodeTemp.parent
                    papa.EditRemaining(papa.remaining-1)
                    hijos = nodeTemp.son
                    nodeTemp.EditRemaining(len(hijos))
                    for hijo in hijos:
                        stack.append(hijo)
                else:
                    hijos = nodeTemp.son
                    nodeTemp.EditRemaining(len(hijos))
                    for hijo in hijos:
                        stack.append(hijo)
    print("To view the tree, enter the following string in http://ironcreek.net/syntaxtree/")
    print()
    print(result)
    print()
            

SelectFile()