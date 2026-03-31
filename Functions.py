"""
Write a function that greets the user by name.
"""

# def greet(name):
#    return(f"Hello {name}")

# print(greet("Sam"))
"""
#Create a function that calculates the area of a rectangle. 
# If no height is provided, assume it’s a square.
"""
# def area(length,height=None):
#     if height :
#         return(height*length)
#     else:
#        return(length*length)
# print(area(height=10,length=20))
# print(area(4))
"""
Write a function to calculate simple interest.
"""
# def simple_interest(principle,rate,time):
#     return(principle * rate * time)/100

# print(simple_interest(1000, 6.5, 5)) 
"""
Write a function that returns both the sum and average of a list
"""
# def stats(numbers):
#     total=sum(numbers)
#     avg=total/len(numbers)
#     return(total,avg)
# result=stats([10,20,40])
# print(f"Sum = {result[0]},Average ={result[1]}")
"""
Write a function to square numbers in a list using map and a lambda.
"""
# numbers=[2,8,6]
# square=list(map(lambda x:x**2,numbers))
# print(square)
"""
Write a function to calculate factorial using recursion
"""
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     return n*factorial(n-1)
# print(factorial(4))
"""
Write a function that takes multiple numbers and returns their product.
"""
# def products(*numbers):
#     product=1
#     for num in (numbers):
#         product *=num
#     return product
# print(products(12,4,5))
"""
Write a function to print employee details using keyword arguments.
"""
def employee_Detail(**details):
    for key,value in details.items():
        print(f"{key} : {value}")
employee_Detail(name="Ravi", age=30, department="IT")