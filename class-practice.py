# # # str = input("Enter a string: ")
# # # print("The typed string is: ",str)
# # # new_str = str.replace(".", "").replace(",", "").replace("?", "")
# # # print("The new string without punctuation marks is: \n",new_str)

# # # Get the key of a minimum value from the following dictionary
# # # class_no = {
# # #        "Asad": 1,
# # #        "Aqib": 2,
# # #        "Ali": 3,
# # #        "Aqsa": 4
# # # }
# # # print(class_no)

# # string = input("Type a string to count no of characters: ")
# # for i in range(len(string)): #find lenght of the string if 
# # #lenght 4 so range will be range(4) = [0,1,2,3] loop will run 4 times
    
# #     char = string[i] #take char at i index number
# #     count = 0   #it counts the character occurence for each character for every new character the counter become 0 again
# #     for j in range(len(string)):#again go through all characters
# #         if string[j] == char: #chechk if current character from outer loop matches at how much positions
# #            count += 1         #count the no of times each character occur
# #     if char not in string[:i]: #this line avoids duplicates
# #         print(char, ":", count)

# def greet(name):
#     print(f"Hello {name}")

# greet("Haroon")

# def even(num):
#     if num % 2 == 0:
#         print(f"The {num} is Even.")
#     else:
#      print("Not even")

# def odd(num):
#     if num % 2 != 0:
#         print(f"The {num} is odd.")
#     else:
#         print("Not odd.")

# odd(3)
# even(5)

# def factorial(num):
#     if num == 0:
#         print("factorial is 1")
#     fact = 1
#     original_num = num
#     while num > 0:
#             fact = fact * num
#             num -= 1
#     print(f"Factorial of {original_num} is:", fact)


# factorial(0)
# factorial(6)

# def table(num, upto):
#     # Store the original number to use in the print statement
#     original_num = num
    
#     # Use a separate counter for the multiplication
#     counter = 1

#     while counter <= upto:
#         result = original_num * counter
#         print(f"{original_num} * {counter} = {result}")
#         counter += 1

# table(4, 5)

# def prime_upto(num):
#     for i in range(2, num+1):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
        
#           print(i,"is Prime number.")

# prime_upto(45)

#NumPy practice
import numpy as np

a = np.arange(20).reshape(4,5)
print(a)
b = np.arange(150).reshape(50,3)
print(b)
