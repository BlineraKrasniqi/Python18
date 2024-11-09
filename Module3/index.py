#Create a set using curly braskets
from calendar import different_locale

#my_set = {1,2,3}

#print(my_set)

#Creting a set from a list using the set() function



my_set ={1,1,2,3,3,4,5,3,2,3}
print(my_set) #Set will automaticlly remove duplicates



################

set1 = {1,2,3}
set2 = {1,2,3}

#Union between set1 and set2 using the union() method
union_method = set1.union(set2)

#Compute union between set1 and set2 using the operator

print("Union of set1 and set2 using method:", union_method)
print("Union of set1 and set2 using method:", union_method)

#Compute intersection between set 1 and set2 using the intersection() method

intersection_method = set1.intersection(set2)

#Computing intersection between set 1 and set2 using

intersection_operator= set1 & set2

print("Intersection of set1 and set2 using the intersection method" intersection_method)
print("Intersection of set1 and set2 using the intersection operator" intersection_operator

#Computing the elements that are unique to set1 to set 1 using the difference method
different_method = set1.difference(set2)

#Computing elements that are unique to set1 using the - operator
different_operator = set1 - set2

print("Difference of set1 and set2 using the difference method:", different_method)
print("Difference of the set1 and set2 using the - operator:" different_operator)

#Copmuting the elements that are in set 1 and set 2 but not in their intersection
symmetric_difference_method = set1.symmetric_difference(set2)

#Computing the elements that are in set1 and in set2 but not in their intersection using the ^ method
symmetric_difference_operator = set1 ^ set2

print("Symmetric difference of set 1 and set 2 using the symmetric difference method:", symmetric_difference_method)
print("Symmetric difference of set 1 and set 2 using the symmetric difference operator: ", symmetric_difference_method)