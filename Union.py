#Python program to illustrate Union
#Maintain Repetition
def Union(list1 , list2):
    final_list = list1 + list2
    return final_list
#Driver code
list1 = [23,15,2,14,14,16,20,52]
list2 = [2,42,15,12,26,32,47,54]
print("Given listd are:", list1, list2)
print("Maintained Repetition")
print(Union(list1,list2))

#Python program to illustrate Union
#Maintain both Repetation and order
def Union(list1,list2):
    final_list=sorted(list1+list2)
    return final_list
#Driver code
list1 = [23,15,2,14,14,16,20,52]
list2 = [2,48,15,12,26,32,47,54]
print("Given lists are: ", list1, list2) 
print("Maintained Repetition and Order")
print(Union(list1,list2))

#python program to illustrate union
#Without Repetition
def Union (list1,list2):
    final_list=list (set(list1)|set(list2))
    return final_list
#Driver code
list1 = [23,15,2,14,14,16,20,52]
list2 = [2,42,15,12,26,32,47,54]
print("Given lists are: ", list1, list2)
print("Without Repetition")
print(Union(list1,list2))

#python program to illustrate union
#Union of three lists
def Union(list1,list2,list3):
    final_list = list(set().union(list1,list2,list3))
    return final_list
#Driver code
list1 = [23,15,2,14,14,16,20,52]
list2 = [2,42,15,12,26,32,47,54]
list3 = [4,78,5,6,9,25,64,32,59]
print("Given lists are: ", list1, list2, list3)
print("Union of three lists")
print(Union(list1,list2,list3))
