#List Manipulation

#Question No 1
#Reverse a list in Python

mix_list = [3.24,'apple', 'banana', 'cherry', 'guava', True, 24]
print("Original order of the list is: ",mix_list)
#to reverse list items python uses reverse function

mix_list.reverse()
print("Reversed order of the list is: ",mix_list)

#lets again give order to the list in another method
new_list = mix_list[::-1]
print("Re arranging list to it original order through other method: ",new_list)

#Question No 2
#Turn every item of a list into its square

num_list = [1, 2, 3, 4, 5, 6]
print("Given list is: ",num_list)
square = [] #taking empty list so that to save square values in it
for i in num_list: #take indexes of num_list
    square.append(i**2)  #taking square of each index of num_list and appending it in square list
print("Square of the given list is: ",square)

#Question No 3
#Remove empty strings from the list of strings

str_list = ['ali', '', 'haroon', 'hashir']
print("List with empty string: ", str_list)
str_list.remove('')
print("The list after removing empty string is: ",str_list)

#Question No 4
#Add new item to list after a specified item

cities = ['lahore', 'peshawar', 'islamabad', 'karachi']
print("The list of cities is: ", cities)
cities.insert(2, 'Faisalabad') #insert help us to add into list at particular index 
print("After adding new city at index[2], the list now is: ",cities)

#but if we want to insert after specified item then first 
# we have to find item at that index 
index = cities.index('peshawar')#first find specified item
cities.insert(index + 1, 'Multan')#then insert after one index after that item
print("Now here adding new city after peshawar: ",cities)

#Question No 5
#Replace list’s item with new value if found

item = [2.13, 'khalid', 12, True, [1,2,3]]
print("List of item is: ",item)
if 'khalid' in item:
   index = item.index('khalid') #finding khalid
   item[index] = 'ali' #replacing khalid with ali
print("List now is: ",item)
