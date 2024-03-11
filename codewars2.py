def numbers_triangle(n=10):
    count = 0
    for i in range(0, n):
        for l in range(0, i + 1):
            print(count, sep=" ", end=" ")
            count += 1
        print(" ")


def comp(array1, array2):
    if not array1 or not array2:
        return False
    zip_arrays = zip(sorted(array1), sorted(array2))
    for a, b in zip_arrays:
        if a * a == b:
            continue
        else:
            return False
    return True


def dna_strand(dna):
    symbols_to_replace = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return ''.join(symbols_to_replace[s] for s in dna if s in symbols_to_replace.keys())

    #second version
    #return dna.translate(str.maketrans("ATCG","TAGC"))


def get_age(age):
    return int(age[0])


def sum_dig_pow(a, b):
    '''
    counter = 1
    sum_dig = 0
    for n in range(a, b + 1):
        for i in range(len(str(n))):
            one_num = str(n)[i]
            x = pow((int(one_num) // 10), (int(one_num) % 10 + 1))
            print(x)
            if sum_dig == n:
                print(n)

    '''

    output_list = []
    for i in range(a, b + 1):
        converted_i = str(i)
        num = 0
        for counter, el in enumerate(converted_i, 1):
            num += int(el) ** counter
        if num == i:
            output_list.append(num)
    print(output_list)


def solution(text, ending):
    text_copy = text[::-1]
    end_text = text_copy[:len(ending)]
    print(end_text)
    if text.endswith(end_text):
        pass
    else:
        return False


import string


def alphabet_position(text):
    alpha_nums = ''
    alphabet = list(string.ascii_lowercase)
    for letter in text.lower():
        if letter in alphabet:
            alpha_nums += str(alphabet.index(letter) + 1) + ' '
    return alpha_nums.rstrip()


def printer_error(s):
    errors = 0
    alphabet = list(string.ascii_lowercase)
    m_index = alphabet.index('m')

    for letter in s:
        if alphabet.index(letter) > m_index:
            errors += 1
    return f'{str(errors)}/{len(s)}'


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


def greet(language):

    '''
    return {
            'czech': 'Vitejte',
            'danish': 'Velkomst',
            'dutch': 'Welkom',
            'english': 'Welcome',
            'estonian': 'Tere tulemast',
            'finnish': 'Tervetuloa',
            'flemish': 'Welgekomen',
            'french': 'Bienvenue',
            'german': 'Willkommen',
            'irish': 'Failte',
            'italian': 'Benvenuto',
            'latvian': 'Gaidits',
            'lithuanian': 'Laukiamas',
            'polish': 'Witamy',
            'spanish': 'Bienvenido',
            'swedish': 'Valkommen',
            'welsh': 'Croeso'
        }.get(language, 'Welcome')
    '''

    db_data = {"english": "Welcome"
                , "czech": "Vitejte"
                , "danish": "Velkomst"
                , "dutch": "Welkom"
                , "estonian": "Tere tulemast"
                , "finnish": "Tervetuloa"
                , "flemish": "Welgekomen"
                , "french": "Bienvenue"
                , "german": "Willkommen"
                , "irish": "Failte"
                , "italian": "Benvenuto"
                , "latvian": "Gaidits"
                , "lithuanian": "Laukiamas"
                , "polish": "Witamy"
                , "spanish": "Bienvenido"
                , "swedish": "Valkommen"
                , "welsh": "Croeso"
                }

    return db_data[language] if language in db_data.keys() else "Welcome"


def human_years_cat_years_dog_years(human_years):
    cat, dog, next_year = 24, 24, human_years - 2
    match human_years:
        case 1:
            return [human_years, cat - 9, dog - 9]
        case 2:
            return [human_years, cat, dog]
        case human_years if human_years > 2:
            return [human_years, cat + next_year * 4, dog + next_year * 5]