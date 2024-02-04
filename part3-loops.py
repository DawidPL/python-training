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

#reversed_list([10, 20, 30, 40, 50])

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

'''
Exercise 11: Write a program to display all prime numbers within a range
'''

def prime_numbers(start_range, end_range):
    print(f'Prime numbers for range {start_range} and {end_range} are:')
    for n in range(start_range, end_range +1):
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n)


'''
Exercise 12: Display Fibonacci series up to 10 terms
'''

def fibo():
    fibo_list = []
    for i in range(10):
        if i == 0 or i == 1 :
            fibo_list.append(i)
        else:
            fibo_list.append((fibo_list[i - 2]) + fibo_list[i-1])
    print (*fibo_list)

    #second version

    num1, num2 = 0, 1
    for i in range(10):
        print(num1, end=" ")
        next_num = num1 + num2

        num1 = num2
        num2 = next_num

'''
Exercise 13: Find the factorial of a given number
'''

def factorial_number(num):
    factorial_number = 1
    for i in range(num, 1 ,-1):
        factorial_number *= i
    print (factorial_number)

'''
Exercise 14: Reverse a given integer number
'''

def reverse_int(number):
    num_to_str = str(number)
    reversed_num = reversed(num_to_str)
    x = ''
    for el in list(reversed_num):
        x += el
    print (x)

    # second version
    reversed_number = 0
    while number > 0:  
        reminder = number % 10
        reversed_number = (reversed_number * 10) + reminder
        number = number // 10
    print(reversed_number)

'''
Exercise 15: Use a loop to display elements from a given list present at odd index positions
'''

def display_odd_index():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for index in range(len(my_list)):
        if index % 2 != 0:
            print (my_list[index])

'''
Exercise 16: Calculate the cube of all numbers from 1 to a given number
'''

def calculate_cube(num):
    for i in range(1, num + 1):
        print(f'Current Number is: {i} and the cume is {i*i*i}')


'''
Exercise 17: Find the sum of the series upto n terms
'''

def find_sum(n, number):
    n_sum = 0
    new_number = 0
    while n > 0:
        n_sum = n * str(number)
        new_number = new_number + int(n_sum)
        n -= 1
    print(new_number)

'''
Exercise 18: Print the following pattern
Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

'''

def print_pattern():
    for i in range(1,6):
        for j in range(1, i+1):
            print('*', end=" ")
        print(" ")
    for i in range(4+1,1, -1):
        for j in range(i,1, -1):
            print('*', end=" ")
        print(" ")
print_pattern()

