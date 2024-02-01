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