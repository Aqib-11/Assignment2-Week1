
#STRING MANIPULATION

#Q1
# Write a program to create a new string made of an input string’s 
# first, middle, and last character.

#logic
#in this program we will take string as input
#then through slicing concept we will slice it
#we will take the first middle and last character afterslicing
# then combine all through + and will assign it a new variable
#then put that variable as new string
#as string can be accessed through indexing

str = input("Type a string: ")

first_char = str[0]
middle_char = str[len(str)//2]  #this will slice string in halft and take the middle character
last_char = str[-1]

new_string = first_char + middle_char + last_char
print("The new string from first, middle and last character is: ", new_string)

# Q2
# Write a program to count occurrences of all characters 
# within a string Given.

#logic
#lets take a string as input and cound its character through 
#nested loop method where for each character it will search
#in first loop and then how many time that character appeared
#it will search in the nested loop

string = input("Type a string to count no of characters: ")
for i in range(len(string)): #find lenght of the string if 
#lenght 4 so range will be range(4) = [0,1,2,3] loop will run 4 times
    
    char = string[i] #take char at i index number
    count = 0   #it counts the character occurence for each character for every new character the counter become 0 again
    for j in range(len(string)):#again go through all characters
        if string[j] == char: #chechk if current character from outer loop matches at how much positions
           count += 1         #count the no of times each character occur
    if char not in string[:i]: #this line avoids duplicates
        print(char, ":", count)


#Q no 3
#Reverse a given string

str = input("Write a string: ")
rev_str = str[::-1]
print("The typed string in reverse order is: ",rev_str)

#Q No 4
#Split a string on hyphens

text = input("Type a string: ")
new_str = text.split() #it split the string in to portion taking each space as a split parameter
new_str = "-".join(new_str) #then joining those words with hypen in new string
print("The typed string now in hyphen is: ",new_str)

# Remove special symbols / punctuation from a string
str = input("Enter a string: ")
print("The typed string is: ",str)
new_str = str.replace(".", "").replace(",", "").replace("?", "")
print("The new string without punctuation marks is: \n",new_str)
