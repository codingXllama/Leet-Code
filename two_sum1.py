

def two_sum(arr,target):
    
    # Creating a dictionary
    myDict = {}
    
    for index in range(len(arr)):
        if target-arr[index] not in myDict:
            myDict[arr[index]]=index
        else:
            # if it already exists in the dictionary
            return [myDict[target-arr[index]],index]



soln=two_sum([1,3,4,10],5)
print(soln)