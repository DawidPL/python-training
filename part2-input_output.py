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
task_six = new_file_generator(5)
print(task_six)