'''
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
'''

def calculation_first(num1, num2):
    if num1 * num2 <= 1000:
        return num1 * num2
    else:
        return num1 + num2
    

#second version
    
def calculation_first_second_ver(num1, num2):
  return num1 * num2 if num1 * num2 <= 1000 else num1 + num2
  
first_task = calculation_first_second_ver(30, 50)  
print (first_task)


'''
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
'''

def calculation_two():
    current_num = 0
    previous_num = 0
    sum_num = 0
    for i in range(10):
        print(f"Current Number {current_num} Previous Number {previous_num} Sum: {sum_num}")
        current_num += 1
        previous_num = current_num - 1
        sum_num = current_num + previous_num

second_task = calculation_two()
print(second_task)


'''
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.
'''

def return_even_elements(string):
    split_string = [* string]
    for i in range(0, len(split_string)):
        if i % 2 == 0:
            print (split_string[i])

# second version with <stride> in range:
            
    for i in range(0, len(split_string), 2):
        print(split_string[i])
        
third_task = return_even_elements('javascript')
print(third_task)


'''
Write a program to remove characters from a string starting from zero up to n and return a new string.
'''

def remove_chars(string, num_of_elements_to_remove):
    split_string = [* string]
    del split_string[0:num_of_elements_to_remove]
        
#second version
    
    while len(split_string) > num_of_elements_to_remove:
        split_string.pop(0)

    new_string = ''.join(split_string)
    return new_string

fourth_task = remove_chars('python', 3)
print(fourth_task)