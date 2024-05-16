import numpy as np
import random

def filling_arrays(million_list, random_list, complex_list, text_list):
    for i in range(0, 999999):
        random_number = random.uniform(-1.0, 1.0)
        random_list.append(random_number)
        million_list.append(i)

    count = 0
    birth_day = 5
    birth_month = 12
    r = birth_day / birth_month
    while count < 420000:
        complex_number = complex(random.uniform(-r, r), random.uniform(-r, r))
        if abs(complex_number) < r**2 or abs(complex_number) == r**2:
            complex_list.append(complex_number)
            count += 1

    file = open("text.txt", "r")
    text = (file.read()).split()
    for word in text:
        text_list.append(word)
    file.close()

    return million_list, random_list, complex_list, text_list


million_list = []
random_list = []
complex_list = []
text_list = []

filling_arrays(million_list, random_list, complex_list, text_list)
