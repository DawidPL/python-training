'''
Exercise 1: Print First 10 natural numbers using while loop
'''

def first_ten_numbers():
    index = 1
    while index <=10:
        print (index)
        index += 1

'''
Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

'''

def print_pattern():
    for i in range(0,6):
        for j in range(1, i+1):
            print(j, end=" ")
        print(" ")


'''
Exercise 3: Calculate the sum of all numbers from 1 to a given number
'''

def sum_all_numbers(num):
    number = 0
    for i in range(1, num):
        number += i
    return number

    # second version

    x = sum(range(1, num+1))

'''
Exercise 4: Write a program to print multiplication table of a given number
'''

def print_multiplication(num):
    list_one = [i * num for i in range(0,10)]
    print (*list_one, sep="\n")

'''
Exercise 5: Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
'''

def display_numbers(list):
    new_list = [i for i in list if i % 5 == 0]
    for i in new_list:
        if i > 500:
            break
        elif i > 150:
            continue
        else:
            print(i)

'''
Exercise 6: Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.
'''

def count_total_number(num):
    if num > 0:
        list_to_str = str(num)
    else:
        # if number is negative
        list_to_str = str(abs(num))

    print (len(list_to_str))
  
'''
Exercise 7: Print the following pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

'''

def print_pattern():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print (j, end=" ")
        print(" ")

'''
Exercise 8: Print list in reverse order using a loop
'''

def reversed_list(list_to_reversed):
    for i in reversed(list_to_reversed):
        print (i)

reversed_list([10, 20, 30, 40, 50])

'''
Exercise 9: Display numbers from -10 to -1 using for loop
'''

def display_negatives():
    for i in range(-10, 0):
        print (i)

'''
Exercise 10: Use else block to display a message “Done” after successful execution of for loop
'''

def display_message():
    for i in range(5):
        print (i)
    else:
        print("done")
