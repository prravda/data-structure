# 2.1
def multable_six():
    for i in range(1, 10):
        print(6 * i)


# 2.2
def multable_six_with_while():
    i = 1
    while i < 10:
        print(6 * i)
        i += 1


# 2.3
def multable_six_reverse():
    for i in reversed(range(1, 10)):
        print(6 * i)


# 2.4
def cel_to_far(cel: int):
    return cel * 1.8 + 32


# 2.5
def far_to_cel(far: int):
    return (far - 32) / 1.8


# 2.6
def reverse_a_list_with_minus_index():
    a = [1, 2, 3, 4]
    for minus_i in range(-1, -len(a) - 1, -1):
        print(a[minus_i])


# 2.7
def sum_of_an_list(l: list[int]) -> int:
    accm = 0
    for e in l:
        accm += e
    return accm


# 2.8
def manipulate_the_string():
    msg = "Data Structures in Python"
    print(msg)
    print(msg.upper())
    print(msg.lower())


# 2.9 and 2.10
def manipulate_dictonary():
    # declare a variable 'price'
    # initialize 'price' with a dictionary
    price = {"haejangguk": 4500, "galbitang": 9000, "pork cutlet": 8000}
    # add pad thai: 7000 (k-v) into this dictionary
    price["pad thai"] = 7000
    print(price)

    # 500krw off each menu
    for menu in price:
        price[menu] -= 500
    print(price)


# 2.11
def sum_with_recursion(n):
    if n == 1:
        return 1
    return n + sum_with_recursion(n - 1)


# 2.12
def harmonic_series_recursion(n):
    if n <= 0:
        return 0
    return 1.0 / n + harmonic_series_recursion(n - 1)


# 2.13
def binomial_coefficient(n, k):
    if k == n or k == 0:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


# 2.14
# reference: https://www.geeksforgeeks.org/binomial-coefficient-dp-9/
def binomial_coefficient_with_loop(n, k):
    c = [[0 for x in range(k + 1)] for x in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
    return c[n][k]


# 2.15
def reverse_the_string(s: str):
    if len(s) == 0:
        return s
    return reverse_the_string(s[1:]) + s[0]


# 2.16
def print_num_asc(n):
    if n == 0:
        return
    print_num_asc(n - 1)
    print(n)


def print_num_desc(n):
    print(n)
    if n == 1:
        return
    print_num_desc(n - 1)


# 2.17
def fibo_with_frequency_checker(till: int):
    checker = {}

    def fibo_nth(n):
        # checker logic
        if checker.get(n) is None:
            checker[n] = 1
        else:
            checker[n] += 1

        if n == 1 or n == 2:
            return 1
        return fibo_nth(n - 1) + fibo_nth(n - 2)

    fibo_nth(till)
    print(checker)


fibo_with_frequency_checker(10)
