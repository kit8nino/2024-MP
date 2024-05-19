import random
import re

def filling_arrays(million_list, random_list, complex_list, text_list):
    for i in range(0, 1000000):
        million_list.append(i)
    random.shuffle(million_list)

    for i in range(0, 99999):
        random_number = random.uniform(-1.0, 1.0)
        random_list.append(random_number)

    count = 0
    birth_day = 5
    birth_month = 12
    r = birth_day / birth_month
    while count < 42000:
        complex_number = complex(random.uniform(-r, r), random.uniform(-r, r))
        if abs(complex_number) <= r:
            complex_list.append(complex_number)
            count += 1

    file = open("text.txt", "r")
    text = file.read()

    pattern = r"[^\w\s]"
    clean_text = re.sub(pattern, "", text)
    clean_text = clean_text.split()

    for word in clean_text:
        text_list.append(word)
    file.close()

    return million_list, random_list, complex_list, text_list
