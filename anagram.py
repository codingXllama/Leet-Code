str1="heart"
str2="earth"

sorted_str1=sorted(str1)
sorted_str2=sorted(str2)

str1=str1.replace(" ","")
str2=str2.replace(" ", "")

#comapring the sorted strings

#checking based on len:
if len(str1)==len(str2):
    if sorted_str1 == sorted_str2:
        print("Anagrams")
    else:
        print("Not anagrams")