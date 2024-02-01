'''
Exercise 1: Accept numbers from a user
Write a program to accept two numbers from the user and calculate multiplication

'''

def input_multiplication():
    input_one = input("Podaj liczbę:")
    input_two = input("Podaj drugą liczbę:")
    return int(input_one)* int(input_two)

task_one = input_multiplication()
print(task_one)

'''
Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.
'''

def string_display(string_one, string_two, string_three):
    print(string_one, string_two, string_three, sep='**')

task_two = string_display('Name', 'Is', 'David')
print(task_two)

'''
Exercise 3: Convert Decimal number to octal using print() output formatting
'''

def decimal_converter(num):
    print('%o' % num) 

task_three = decimal_converter(8)
print(task_three)