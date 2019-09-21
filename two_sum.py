'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


# def two_sum(nums,target):

#     leftVal_posn=0
#     rightVal_posn=len(nums)-1

#     #Time complexity : O(n)
#     #Space Complexity: O(1)

#     #Going through the elemnts in the list(nums)
#     for item in range(len(nums)):
#         if nums[leftVal_posn]+nums[rightVal_posn]==target:
#             print("True")
#             return [nums[leftVal_posn],nums[rightVal_posn]]
        
#         elif nums[leftVal_posn]+nums[rightVal_posn]>target:
#             rightVal_posn-=1
        
#         elif nums[leftVal_posn]+nums[rightVal_posn]<target:
#             leftVal_posn+1
        




#Hash table method

def two_sum(nums,target):
    
    ht=dict()

    for item in range(len(nums)):
        if nums[item] in ht:
            return [ht[nums[item]],item-1]
        else:
            ht[target-nums[item]]=nums[item]
    return False


myArr=[2,7,11,15]
print(two_sum(myArr,9))