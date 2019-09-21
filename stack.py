#Creating a stack data structure

class Stack():
    #Creating the class constructor
    def __init__(self):
        # Creating an empty stack
        self.myStack=[]

    #Creating the push operation
    def push(self,element):
        self.myStack.append(element)

    #creating the pop operation
    def pop(self):
        return self.myStack.pop()
    

    #viewing the stack, we just return the stack! (self.myStack)
    def ViewStack(self):
        return self.myStack

    
    def isEmpty(self):
        return self.myStack==[]
        
    #to view the top element
    def peakStack(self):
        #first we must check if the stack is empty
        if not self.isEmpty():
            return self.myStack[-1]



#Test
newStack= Stack() #Creating a stack object
newStack.push('A')
newStack.push('C')
print(newStack.ViewStack())
newStack.push('D')
print(newStack.ViewStack())
newStack.pop()
print(newStack.ViewStack())
#checking if the stack is empty
print(newStack.isEmpty())
#getting the top elment
print(newStack.peakStack())