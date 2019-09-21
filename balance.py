#To determine if a parenthesis is balanced

class Stack():
    def __init__(self):
        self.myStack=[]
    
    def push(self,element):
        self.myStack.append(element)
    
    def pop(self):
        return self.myStack.pop()
    
    def isEmpty(self):
        return self.myStack == []
    
    def PeakStack(self):
        if not self.isEmpty():
            return self.myStack[-1]

    def ViewStack(self):
        return self.myStack




#Creating the balance parthenthesis 
'''

Balanced : {[()]}
Not-Balanced: (()
Not-Balanced: ))


( ) -> isMatch(topParen,currentParen)

(
[
{ 

'''


def isMatched(p1,p2):
    if p1=='(' and p2==')':
        return True
    elif p1=='{' and p2=='}':
        return True
    elif p1=='[' and p2==']':
        return True
    else:
        return False


def is_paren_balanced(paren_arr):


    
    #creating a stack object
    myStack=Stack()
    isBalanced=True
    currentIndex=0

    #looping throught the string arr
    while currentIndex<len(paren_arr) and isBalanced:
        #storing the left most paren from the given string
        paren=paren_arr[currentIndex]
        #checking the left_paren type
        if paren in "([{":
            myStack.push(paren)
        else:
            if myStack.isEmpty():
                isBalanced=False
            else:
                #to get the top most element, use the pop operation
                topElement=myStack.pop()
                if not isMatched(topElement,paren):
                    isBalanced=False
             
        currentIndex+=1

    #checking if the stack is empty
    if myStack.isEmpty() and isBalanced:
        return True
    
    else:
        return False

            



print(is_paren_balanced("([(])"))






# newStack= Stack() #Creating a stack object
# newStack.push('A')
# newStack.push('C')
# print(newStack.ViewStack())
# newStack.push('D')
# print(newStack.ViewStack())
# newStack.pop()
# print(newStack.ViewStack())
# #checking if the stack is empty
# print(newStack.isEmpty())
# #getting the top elment
# print(newStack.PeakStack())