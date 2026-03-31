"""
IF-ELIF-ELSE Statement (Question 9)
 Shweta is grading students. Marks are classified as:


90+ = Grade A


75–89 = Grade B


50–74 = Grade C


Below 50 = Fail
 Write a Python program for this grading system.

"""
# name=input("Enter the name of the student :")
# marks=float(input(f"Enter the marks for {name}:"))
# result=None
# if(marks>=90 and marks<=100):
#     result="Grade A"
#     print(f"{name} has achieved {result} with marks:{marks},congrats")
# elif(marks>=75 and marks<=89 ):
#     result="Grade B"
#     print(f"{name} has achieved {result} with marks:{marks},keep going")
# elif(marks>=50 and marks<=74 ):
#     result="Grade C"
#     print(f"{name} has achieved {result} with marks:{marks},Study well")   
# elif (marks>=0 and marks<50 ):
#     result="Failed"
#     print(f"{name} has  {result} with marks:{marks}")
# else:
#     print(f"Please check your input,Marks:{marks}")
"""
MATCH Case Statement (Question 11)
 Sita is running a bookstore. Customers ask for 
 categories: “Fiction”, “Non-Fiction”, or “Comics”,"History". 
 Print the section where the book can be found. Write a Python program using match.
"""
#member=input("Enter the membership:")
#category=input("Enter the category of book you want:")
# match category:
#     case "Fiction":
#         print(f"{category} is on first floor room no:4A")
#     case "Non-Fiction":
#         print(f"{category} is on first floor room no:3A")
#     case "Comics":
#         print(f"{category} is on first floor room no:2A")
#     case "History":
#         print(f"{category} is on first floor room no:5A")
#     case _:
#         print(f"{category} not found! Pleasetry again!!")
# if category=="Fiction":
#    print(f"{category} is on first floor room no:4A")
# elif category=="Non-Fiction":
#    print(f"{category} is on first floor room no:2A")
# elif category=="Comics":
#    print(f"{category} is on first floor room no:3A")
# elif category=="History":
#    print(f"{category} is on first floor room no:5A")
# else:
#   print(f"{category} not found! Pleasetry again!!")
"""
Print table for  a number
"""
#number=int(input("Enter a number for table:"))
# for i in range (1,21):
#     print(f" {number}* {i}  = {number * i}")
# limit=1
# while limit<=20:
#      print(f" {number}* {limit}  = {number * limit}")
#      limit+=1
"""
Meena guessing game
"""
correct_guess=7
while True:
     player_guess=int(input(f"Enter your guess:"))
     if player_guess == correct_guess :
          print("You  have won the game !!!")
          break
     else:
          print("Try again!!")
