'''
Exercise 1: Accept numbers from a user
Write a program to accept two numbers from the user and calculate multiplication

'''

def input_multiplication():
    input_one = input("Podaj liczbę:")
    input_two = input("Podaj drugą liczbę:")
    return int(input_one)* int(input_two)


'''
Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.
'''

def string_display(string_one, string_two, string_three):
    print(string_one, string_two, string_three, sep='**')


'''
Exercise 3: Convert Decimal number to octal using print() output formatting
'''

def decimal_converter(num):
    print('%o' % num) 

'''
Exercise 4: Display float number with 2 decimal places using print()
'''

def truncate(num):
    return round(num, 2)

'''
Exercise 5: Accept a list of 5 float numbers as an input from the user
'''

def get_five_numbers():
    float_list = []
    for _ in range(5):
        x = float(input("Podaj liczbę:"))
        float_list.append(x)
    return float_list


'''
Exercise 6: Write all content of a given file into a new file by skipping line number 5
'''

def new_file_generator(line_to_remove):
    with open('text.txt', 'r') as f:
        lineindex = 0
        file_lines = f.readlines()
    with open('new_text.txt', 'w') as new_f:
        for text_line in file_lines:
            if lineindex == line_to_remove:
                lineindex += 1
                continue
            else:
                new_f.write(text_line)
            lineindex += 1

'''
Exercise 7: Accept any three string from one input() call
Write a program to take three names as input from a user in the single input() function call.
'''

def multistring_input():
    names = input('Enter 3 names separeted by space: ')
    split_names = names.split(',')
    for name in split_names:
        print(f'Name{split_names.index(name) + 1} {name}')

'''
Exercise 8: Format variables using a string.format() method.
Write a program to use string.format() method to format the following three variables as per the expected output
'''

def string_format():
    total_money = 1000
    quantity = 3
    price = 450
    print('I have {totalmoney} so I can buy {quantity} for {price}'.format(totalmoney=total_money, quantity=quantity, price=float(price)))


'''
Exercise 10: Read line number 4 from the following file
'''

def read_line():
    with open('text.txt', 'r') as f:
        lines = f.readlines()
        print(lines[3])

read_line()