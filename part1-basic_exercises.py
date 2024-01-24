'''
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
'''

def calculation(num1, num2):
    if num1 * num2 <= 1000:
        return num1 * num2
    else:
        return num1 + num2
    

#second version
    
def multiplication_or_sum(num1, num2):
  return num1 * num2 if num1 * num2 <= 1000 else num1 + num2
  
return_value = multiplication_or_sum(30, 50)  
print (return_value)
