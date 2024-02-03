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

display_numbers([12, 75, 150, 180, 145, 525, 50])