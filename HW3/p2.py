#Importing the mergesort function from p1.py

from p1 import mergeSort
def isAnagram(s, t):
    #change the two text to lower letters
    s=s.lower()
    t=t.lower() 

    #convert the strings to numbers
    s_list=[ord(i) for i in s]
    t_list=[ord(j) for j in t] 

    #use the mergesort function from p1
    s = mergeSort(s_list) 
    t = mergeSort(t_list) 

    #Getting the length
    n1 = len(s)  
    n2 = len(t)  
 
    #Checking if the length are equal,if not return false
    if n1 != n2:  
        return 0

    #checking the corresponding letters in each position,
    #if they are equal, return 1, if not return 0
    for i in range(0, n1):  
        if s[i] != t[i]:  
            return 0
    return 1
  
#test 
s = "hecn"
t = "chen"

#If true, return true; if false, return false
if isAnagram(s, t):  
    print ("True")
else:  
    print ("False") 