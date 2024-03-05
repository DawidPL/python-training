from icecream import ic
import time as tm
import math


def even_odd(x):
    return f'odd' if x % 2 == 0 else f'even'


def sum_list(x):
    return f'{sum(x)}'


def reverse_string(x: str):
    return x[::-1]


def if_palidrom(name: str) -> bool:
    return name == name[::-1]


def find_factorial(num):
    counter = 0
    factorial = 1
    if num == 1:
        return factorial
    else:
        while counter != num:
            counter += 1
            factorial *= counter
        return factorial


def check_if_prime(num):
    flag = False
    if num == 1:
        print(num, 'is not a prime num')
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            print(num, 'is not prime')
        else:
            print(num, 'is prime')


def fibonacci(num):
    num1 = 0
    num2 = 1
    next_num = num2
    for i in range(2, num):
        print(next_num)
        num1, num2 = num2, next_num
        next_num = num1 + num2


def move_zero():
    li = [22, 34, 1, 0, 4]
    return sorted(li, reverse=True)


def remove_duplicated_elements(l: list) -> None:
    list_len = len(l)
    counter = 1
    for el in range(1, list_len):
        if l[el] != l[el - 1]:
            l[counter] = l[el]
            counter += 1
    print(counter)


def time_decorator(func):
    def wrapper(*args, **kwargs):
        before = tm.time()
        value = func(*args, **kwargs)
        after = tm.time()
        print(f'Czas wykonania funkcji:{after - before}')
        return value
    return wrapper


@time_decorator
def largest_num(x):
    number = 0
    for n in x:
        if number < n:
            number = n
    return number


def namedtuple_example():
    from typing import NamedTuple
    class T(NamedTuple):
        a: int
        b: int
        c: str
    x = T(40, 20, 'Dawid')
    y = x.b
    print(y)


def sum_of_previous_nums(l: list[int]) -> list[int]:
    new_l = []
    el_sum = 0
    for el in range(0, len(l)):
        el_sum += l[el]
        new_l.append(el_sum)
    print(new_l)
    return new_l


#  Roman to Integer
def roman_to_int(number: str) -> int:
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_dict_optional = {'IV': 4, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'XI': 11, 'XII': 12, 'XIII': 13, 'XL': 40,
                         'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90, 'CD': 400, 'DC': 600, 'DCC': 700, 'DCCC': 800,
                         'CM': 900}
    number_split = list(number)
    int_sum = 0
    optional_val = 0
    for el in range(len(number_split) - 1):
        if rom_dict[number[el]] < rom_dict[number[el + 1]]:
            int_sum -= rom_dict[number[el]]
        else:
            int_sum += rom_dict[number[el]]

    return int_sum


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = tm.perf_counter()
        tm.sleep(4)
        value = func(*args, **kwargs)
        end = tm.perf_counter()
        real_time = end - start
        print(f'{real_time:.1f}t')
        return value
    return wrapper


'''
def first_non_consecutive(arr):
    num1 = 0
    num2 = 0
    for num in arr:
        num1 = num
        if num1 - num2 != 1:
            return num
        else:
            num2 = num1

'''


def first_non_consecutive(a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None


def nb_year(p0, percent, aug, p):
    years = 0
    updated_p = 0
    population = p0
    while population <= p:
        year = float(population) + (float(population) * (percent / 100)) + float(aug)
        population = math.floor(year)
        print(population)
        years += 1
        print(years)

    print(years)


def number(bus_stops):
    return sum(i - o for i, o in bus_stops)

'''
def accum(st):
    str_list = [s for s in st]
    for count, letter in enumerate(range(len(str_list)), start=1):
        str_list[letter] = (str_list[letter] * count).capitalize()
    new_list = '-'.join(str_list)
    print(new_list)
accum('Dawid')
'''


def accum(st):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


def reverse_words(text):
    list_of_words = text.split(' ')
    for count, word in enumerate(list_of_words):
        list_of_words[count] = word[::-1]

    print(' '.join(list_of_words))


from functools import reduce


def find_short(s):
    string_list = s.split(' ')
    print(string_list)
    print (reduce(lambda a, b: a if len(a) < len(b) else b, string_list))


'''
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29

'''


def row_sum_odd_numbers(n):
    iter_n = 0
    odd_list = []
    i = 0
    for x in range(1, n+1):
        iter_n += x

    while len(odd_list) != iter_n:
        if i % 2 != 0:
            odd_list.append(i)
        i += 1
    slice_list = odd_list[-n:]
    print(sum(slice_list))


def likes(names):
    len_name = len(names)
    match names:
        case len_name if len(names) == 0:
            return "no one likes this"
        case len_name if len(names) == 1:
            return f"{names[0]} likes this"
        case len_name if len(names) == 2:
            return f"{names[0]} and {names[1]} like this"
        case len_name if len(names) == 3:
            return f"{names[0]}, {names[1]} and {names[3]} like this"
        case len_name if len(names) > 3:
            return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
    print(len(names))
    print(type(names))


from collections import Counter


def duplicate_count(text):
    counter = 0
    counter_letter = Counter(text.lower())
    for letter in counter_letter.items():
        if letter[1] >= 2:
            counter += 1
    return counter


def is_square(n):
    return math.sqrt(n).is_integer() if n >= 0 else False


def longest_consec(str_list, k):
    word = ''
    if str_list and (len(str_list) > k >= 1):
        for i in range(len(str_list) - k):
            res = min(str_list, key=len)
            str_list.remove(res)
        for i in str_list:
            word += i
        return word
    else:
        return ""


def find_it(seq):
    counter = 0
    for i in seq:
        int_count = seq.count(i)
        if (int_count > counter) and (int_count % 2 != 0):
            counter = i
    print(counter)


from itertools import groupby


def unique_in_order(iterable):
    print([k for (k, _) in groupby(iterable)])


def reverse_string(sentence):
    ls = ' '.join((sentence.split(' '))[::-1])
    print(ls)


def tower_builder(n_floors):
    if n_floors == 0:
        return []
    result = []

    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        space = ' ' * (n_floors - i)
        result.append(space + stars + space)
    print(result)


def sort_array(source_array):
    odd_list = sorted([el for el in source_array if el % 2 != 0])
    i = 0
    for el in range(len(source_array)):
        if source_array[el] % 2 != 0:
            source_array[el] = odd_list[i]
            i += 1
    print(source_array)


from itertools import combinations


def matching_pairs(lst: list[int], target: int) -> None:
    comb = combinations(lst, 2)
    for pair in comb:
        if pair[0] + pair[1] == target:
            print(f'{pair[0]} and {pair[1]}')


def remove_smallest(numbers):
    if numbers:
        copy_numbers = numbers.copy()
        copy_numbers.remove(min(copy_numbers))
        return copy_numbers
    else:
        return []


def twice_as_old(dad_years_old, son_years_old):
    double_son_years = 2 * son_years_old
    return dad_years_old - double_son_years if dad_years_old >= double_son_years else double_son_years - dad_years_old
    # return abs(dad_years_old - 2*son_years_old)


def quarter_of(month):
    match month:
        case month if 1 <= month  < 4:
            return 1
        case month if 4 <= month  < 7:
            return 2
        case month if 7 <= month  < 10:
            return 3
        case month if 10 <= month  <= 12:
            return 4
    # return ceil(month / 3)


def duplicate_encode(word):
    code = ''
    lower_word = word.lower()
    for el in lower_word:
        print(el)
        if lower_word.count(el) == 1:
            code += "("
        else:
            code += ")"
    print(code)


def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    else:
        if (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'rock' and p2 == 'scissors'):
            return f'Player 1 won!'
        else:
            return f'Player 2 won!'


def count_smileys(arr):
    smiles_list = [':)', ';)', ':D', ';D', ':-)', ';-)', ':~)', ';~)', ':-D', ';-D', ':~D', ';~D']
    return sum(int(1) for el in arr if el in smiles_list)

# second version
#from re import findall
    #return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))


from itertools import permutations


def two_sum(numbers, target):
    perm = permutations(numbers, 2)
    perm_list = list(perm)
    numbers_list = []
    for counter, p in enumerate(perm_list):
        if p[0] + p[1] == target:
            multi_check = lambda x, y: 1 if x == y else 0
            numbers_list.append([numbers.index(p[0]), numbers.index(p[1], multi_check(p[0], p[1]))])
    print(numbers_list)


def is_pow_of_four(number):
    for n in range(1, number):
        if pow(n, 4) == number:
            return n
    return False

is_pow_of_four(16)