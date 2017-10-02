#Merge two sorted lists into one new sorted list

#First list made and then sorted
list1 = [1, 6, 4]
list1.sort()

#Second list made and then sorted
list2 = [2, 5, 3]
list2.sort()

#Both sorted lists merged and sorted again
merge = list1 + list2
merge.sort()

#Output the merged and sorted list
print(merge)