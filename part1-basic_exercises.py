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
Exercise 4: Write a program to remove characters from a string starting from zero up to n and return a new string.
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

'''
Exercise 5: Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
'''

def compare_list_element(list):
    if list[0] == list[-1]:
        return True
    else:
        return False

fifth_task = compare_list_element([10, 20, 30, 20, 20, 20]) 
print (fifth_task)

'''
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5
'''

def divisible_numbers(list):
    for i in list:
        if i % 5 == 0:
            print (i)

task_six = divisible_numbers([20, 40, 22, 30, 21])
print(task_six)

'''
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.
'''

def substring_counter(string):
    splitter_string = string.split(' ')
    counter = 0
    for item in splitter_string:
        if item == "Emma":
            counter += 1
    print (f'Emma in this string appear {counter} times')

task_seven = substring_counter("Emma in this sentece appear 2 times. Emma is 10 years old")
print (task_seven)

'''
Exercise 8: Print the following patterns:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5


'''

def print_numbers():
    rows = 6

    for i in range(1, rows):
        for j in range(i):
            print(i, sep=" ", end=" ")
        print(" ")

    for i in range(1, rows):
        for j in range(1, i + 1):
            print(j,  sep=" ", end=" ")   
        print(" ")
    
    for i in reversed(range(1, rows)):
        for j in range(i):
            print(i, sep=" ", end=" ")
        print(" ")


task_eight = print_numbers()
print(task_eight)


'''
Exercise 9: Write a program to check if the given number is a palindrome number.
'''

def palidrome(number):
    number_to_list = [* str(number)]
    reversed_list = number_to_list[::-1]
    reversed_number = ''.join(reversed_list)
    if str(number) == reversed_number:
        return True
    else:
        return False

task_nine = palidrome(151)
print(task_nine)

'''
Exercise 10: Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
'''

def new_list(list1, list2):
    new_list = []
    for num in list1:
        if num % 2 != 0:
             new_list.append(num)
    for num in list2:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

task_ten = new_list([10, 20, 25, 30, 35], [40, 45, 60, 75, 90])
print (task_ten)

'''
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
'''

def extract_digit(number):
    num_to_list = [* str(number)]
    reversed_num = reversed(num_to_list)
    digits = " ".join(reversed_num)
    return digits

task_eleven = extract_digit(1234)
print(task_eleven)