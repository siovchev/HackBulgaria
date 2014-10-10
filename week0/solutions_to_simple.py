def nth_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

print(nth_fibonacci(1)
1
print(nth_fibonacci(2)
1
print(nth_fibonacci(3)
2
print(nth_fibonacci(10)
55

def sum_of_digits(n):
    result = 0
    n = abs(n)
    while n > 0:
        result += n % 10
        n /= 10
    return result

print(sum_of_digits(1325132435356)
43
print(sum_of_digits(123)
6
print(sum_of_digits(6)
6
print(sum_of_digits(-10)
1

def sum_of_divisors(n):
    result = 0
    for divisor in range(1, n / 2 + 1):
        if n % divisor == 0:
            result += divisor
    return result + n

print(sum_of_divisors(8)
15
print(sum_of_divisors(7)
8
print(sum_of_divisors(1)
1
print(sum_of_divisors(1000)
2340

def is_prime(n):
    number = abs(n)
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(1)
False
print(is_prime(2)
True
print(is_prime(8)
False
print(is_prime(11)
True
print(is_prime(-10)
False

def prime_number_of_divisors(n):
    #plus one for n itself
    divisors = 1
    for divisor in range(1, n):
        if n % divisor == 0:
            divisors += 1
    if divisors == 1:
        return False
    if divisors == 2:
        return True
    for i in range(2, divisors):
        if divisors % i == 0:
            return False
    return True

print(prime_number_of_divisors(7)
True
print(prime_number_of_divisors(8)
False
print(prime_number_of_divisors(9)
True

def sevens_in_a_row(arr, n):
    count = 0
    for element in arr:
        if element == 7:
            count += 1
    if count >= n:
        return True
    else:
        return False

print(sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3)
True
print(sevens_in_a_row([1,7,1,7,7], 4)
False
print(sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3)
True
print(sevens_in_a_row([7,2,1,6,2], 1)
True

def is_int_palindrome(n):
    to_str = str(n)
    result = False
    count_of_equal_nums = 0
    for digit in range(0, len(to_str) // 2):
        if to_str[digit] == to_str[len(to_str) - digit - 1]:
            count_of_equal_nums += 1
        if count_of_equal_nums == len(to_str) // 2:
            result = True
    if n == 1:
        return True
    else:
        return result

print(is_int_palindrome(1))
True
print(is_int_palindrome(42))
False
print(is_int_palindrome(100001))
True
print(is_int_palindrome(999))
True
print(is_int_palindrome(123))
False

def contains_digit(number, digit):
    while number > 0:
        if number % 10 == digit:
            return True
        number /= 10
    return False

    # number_to_str = str(number)
    # digit_to_str = str(digit)
    # if digit_to_str in number_to_str:
    #     return True
    # else:
    #     return False

print(contains_digit(123, 4)
False
print(contains_digit(42, 2)
True
print(contains_digit(1000, 0)
True
print(contains_digit(12346789, 5)
False

def contains_digits(number, digits):
    count = 0
    for digit in digits:
        if str(digit) in str(number):
            count += 1
        if count == len(digits):
            return True
    if len(digits) == 0:
        return True
    else:
        return False

print(contains_digits(402123, [0, 3, 4])
True
print(contains_digits(666, [6,4])
False
print(contains_digits(123456789, [1,2,3,0])
False
print(contains_digits(456, [])
True

def is_number_balanced(n):
    to_str = str(n)
    left_side = 0
    right_side = 0

    if len(to_str) == 1:
        return True
    if len(to_str) == 2:
        if int(to_str[0]) == int(to_str[1]):
            return True
        else:
            return False

    for digit in range(0, len(to_str) / 2):
        left_side += int(to_str[digit])
        right_side += int(to_str[len(to_str) - digit - 1])

    if left_side == right_side:
        return True
    else:
        return False


print(is_number_balanced(9)
True
print(is_number_balanced(11)
True
print(is_number_balanced(13)
False
print(is_number_balanced(121)
True
print(is_number_balanced(4518)
True
print(is_number_balanced(28471)
False
print(is_number_balanced(1238033)
True

def count_substrings(haystack, needle):
    result = haystack.count(needle)
    return result

print(count_substrings("This is a test string", "is")
2
print(count_substrings("babababa", "baba")
2
print(count_substrings("Python is an awesome language to program in!", "o")
4
print(count_substrings("We have nothing in common!", "really?")
0
print(count_substrings("This is this and that is this", "this")  # "This" != "this"
2

def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for letter in text:
        if letter.lower() in vowels:
            count += 1
    return count

print(count_vowels("Python")
2
print(count_vowels("Theistareykjarbunga") #It's a volcano name!
8
print(count_vowels("grrrrgh!")
0
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
22
print(count_vowels("A nice day to code!")
8

def count_consonants(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for letter in text:
        if letter.lower() not in vowels and letter.lower().isalpha():
            count += 1
    return count

print(count_consonants("Python")
4
print(count_consonants("Theistareykjarbunga") #It's a volcano name!
11
print(count_consonants("grrrrgh!")
7
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
44
print(count_consonants("A nice day to code!")
6

def number_to_list(n):
    result = []
    to_str = str(n)
    for digit in to_str:
        result.append(digit)
    return result

print(number_to_list(123)
[1, 2, 3]
print(number_to_list(99999)
[9, 9, 9, 9, 9]
print(number_to_list(123023)
[1, 2, 3, 0, 2, 3]

def list_to_number(digits):
    result = 0
    for digit in digits:
        result *= 10
        result += int(digit)
    return result

print(list_to_number([1,2,3])
123
print(list_to_number([9,9,9,9,9])
99999
print(list_to_number([1,2,3,0,2,3])
123023

def biggest_difference(arr):
    result = 0
    for number in arr:
        for second_number in arr:
            if abs(number - second_number) > abs(result):
                result = number - second_number
    return result

print(biggest_difference([1,2])
-1
print(biggest_difference([1,2,3,4,5])
-4
print(biggest_difference([-10, -9, -1])
-9
print(biggest_difference(range(100))
-99

def is_increasing(seq):
    is_monotonous = False
    counter = 0

    if len(seq) == 1:
        return True

    while counter < (len(seq) - 1):
        if seq[counter] < seq[counter + 1]:
            is_monotonous = True
            counter += 1
            continue
        else:
            is_monotonous = False
            break

    return is_monotonous


print(is_increasing([1,2,3,4,5])
True
print(is_increasing([1])
True
print(is_increasing([5,6,-10])
False
print(is_increasing([1,1,1,1])
False

def is_decreasing(seq):
    is_monotonous = False
    counter = 0

    if len(seq) == 1:
        return True

    while counter < (len(seq) - 1):
        if seq[counter] > seq[counter + 1]:
            is_monotonous = True
            counter += 1
            continue
        else:
            is_monotonous = False
            break

    return is_monotonous

print(is_decreasing([5,4,3,2,1])
True
print(is_decreasing([1,2,3])
False
print(is_decreasing([100, 50, 20])
True
print(is_decreasing([1,1,1,1])
False

def zero_insert(n):
    lst = []
    result = 0
    counter = 0

    for digit in str(n):
        lst.append(digit)

    while counter < (len(lst) - 1):
        if lst[counter] == lst[counter + 1] or \
            (int(lst[counter]) + int(lst[counter + 1])) % 10 == 0:
            lst.insert(counter + 1, 0)
        counter += 1

    for digit in lst:
        result += int(digit)
        result *= 10

    result /= 10
    return result


print(zero_insert(116457)
10160457
print(zero_insert(55555555)
505050505050505
print(zero_insert(1)
1
print(zero_insert(6446)
6040406

def sum_matrix(m):
    sum = 0

    for row in m:
        for number in row:
            sum += number

    return sum

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m))
45
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(sum_matrix(m))
0
m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sum_matrix(m))
55


def matrix_bombing_plan(rows, columns, bomb_damage):

    def is_in_matrix(x, y, m):
        if x >= rows or x < 0:
            return False
        if y >= columns or y < 0:
            return False
        else:
            return True

    def add_damage(x, y, m):
        damage = 0
        if m[x][y] - bomb_damage > 0:
            damage = m[x][y] - bomb_damage
        elif m[x][y] - bomb_damage <= 0:
            damage = m[x][y]
        return damage

    max_damage = 0
    current_damage = 0
    damages = {}
    #creating the matrix
    matrix = []
    matrix_element = 1
    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            matrix[row].append(matrix_element)
            matrix_element += 1
    #printing the matrix, while calculating damage
    print()
    for row in range(rows):
        for element in range(columns):
            for i in range(3):
                if is_in_matrix(row - 1, element - 1 + i, matrix):
                    current_damage += add_damage(row - 1, element - 1 + i, matrix)
                if is_in_matrix(row + 1, element - 1 + i, matrix):
                    current_damage += add_damage(row + 1, element - 1 + i, matrix)
            if is_in_matrix(row, element - 1, matrix):
                current_damage += add_damage(row, element - 1, matrix)
            if is_in_matrix(row, element + 1, matrix):
                current_damage += add_damage(row, element + 1, matrix)
            if current_damage > max_damage:
                max_damage = current_damage
            damages[(row, element)] = current_damage
            current_damage = 0
            print(matrix[row][element], end=' ')
        print()
    print()

    for key in damages:
        print(key, end=": ")
        print(damages[key])

matrix_bombing_plan(3, 3, 9)


def next_hack(n):
    n += 1
    #check if it is a palindrome
    to_str = str(bin(n))
    to_str = to_str[2:]
    is_palindrome = False
    equal_digits = 0
    for digit in range(0, len(to_str) // 2):
        if to_str[digit] == to_str[len(to_str) - digit - 1]:
            equal_digits += 1
    if equal_digits == len(to_str) // 2:
        is_palindrome = True
    if n == 1:
        is_palindrome = True

    #check for odd amount of ones
    to_bin = to_str
    ones = 0
    has_odd_amount_of_ones = False
    for digit in to_bin:
        if digit == '1':
            ones += 1
    if ones % 2 != 0:
        has_odd_amount_of_ones = True

    #check if it is a hack number
    is_hack = False

    if has_odd_amount_of_ones is True and is_palindrome is True:
        is_hack = True

    if is_hack is True:
        return n
    else:
        return next_hack(n)


print(next_hack(0))
1
print(next_hack(10))
21
print(next_hack(8031))
8191

def nan_expand(times):
    result = ''
    for time in range(0, times):
        result += 'Not a '
    if times == 0:
        return ''
    return result + 'NaN'

print(nan_expand(0))
""
print(nan_expand(1))
"Not a NaN"
print(nan_expand(2))
"Not a Not a NaN"
print(nan_expand(3))
"Not a Not a Not a NaN"

def iterations_of_nan_expand(expanded):
    iterations = expanded.count("Not a ")
    if expanded != "" and expanded != " " and iterations == 0:
        return False
    #adding length of NaN
    if iterations >= 1 and iterations * 6 + 3 == len(expanded):
        return iterations
    elif expanded == "" or expanded == " ":
        return iterations
    return False

print(iterations_of_nan_expand(""))
0
print(iterations_of_nan_expand("Not a NaN"))
1
print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
10
print(iterations_of_nan_expand("Show these people!"))
False
print(iterations_of_nan_expand("Not a Show these people!"))
False
print(iterations_of_nan_expand(" "))
0

def prime_factorization(n):
    result = []

    for divisor in range(2, n + 1):
        power = 0
        count = 0
        is_prime_divisor = False

        for i in range(2, divisor):
            count += 1
            if divisor % i == 0:
                is_prime_divisor = False
                break
            elif count == divisor - 2:
                is_prime_divisor = True

        if divisor == 2:
            is_prime_divisor = True

        while (is_prime_divisor is True) and n % divisor == 0:
            n /= divisor
            power += 1

        if power != 0:
            result.append((divisor, power))

    return result

print(prime_factorization(10))
[(2, 1), (5, 1)] # This is 2^1 * 5^1
print(prime_factorization(14))
[(2, 1), (7, 1)]
print(prime_factorization(356))
[(2, 2), (89, 1)]
print(prime_factorization(89))
[(89, 1)] # 89 is a prime number
print(prime_factorization(1000))
[(2, 3), (5, 3)]

def calculate_coins(sum):
    change = [100, 50, 20, 10, 5, 2, 1]
    result = {}
    sum_in_coins = int(sum * 100)

    for coin in change:
        while sum_in_coins - coin >= 0:
            if coin not in result:
                result[coin] = 0
            result[coin] += 1
            sum_in_coins -= coin
        if coin not in result:
            result[coin] = 0

    return result


print(calculate_coins(0.53))
{1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0} # We pay with one coin of value 50 and two coins of value 2 and one coin of value 1 - that's the minimal number of coins to get to 0.53
print(calculate_coins(8.94))    
{1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}

def what_is_my_sign(day, month):
    signs = {((21,4), (20,5)): "Taurus", 
             ((21,3), (20,4)): "Aries", 
             ((22,5), (21,6)): "Gemini", 
             ((22,6), (22,7)): "Cancer", 
             ((23,7), (22,8)): "Leo", 
             ((23,8), (23,9)): "Virgo", 
             ((24,9), (23,10)): "Libra", 
             ((24,10), (22,11)): "Scorpio", 
             ((23,11), (21,12)): "Sagittarius", 
             ((22,12), (20,1)): "Capricorn", 
             ((21,1), (19,2)): "Aquarius", 
             ((20,2), (20,3)): "Pisces", }

    for sign_date in signs:
        if month == sign_date[0][1] and day >= sign_date[0][0]:
            return signs[sign_date]
        if month == sign_date[1][1] and day <= sign_date[1][0]:
            return signs[sign_date]

print(what_is_my_sign(5, 8))
"Leo"
print(what_is_my_sign(29, 1))
"Aquarius"
print(what_is_my_sign(30, 6))
"Cancer"
print(what_is_my_sign(31, 5))
"Gemini"
print(what_is_my_sign(2, 2))
"Aquarius"
print(what_is_my_sign(8, 5))
"Taurus"
print(what_is_my_sign(9, 1))
"Capricorn"