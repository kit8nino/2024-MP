import random
data_array=[random.random()*(-1)**random.randint(0,1) for i in range(100000)]
print("Исходный массив данных:\n{}".format(data_array))

def least_significant_digit_sort(data_array):
    
    def digit(number,digits_after_comma):
        num=abs(number)
        x=int(str(num)[digits_after_comma])
        return x
    
    positive = [i for i in data_array if i>0]
    negative = [i for i in data_array if i<0]
    digits_after_comma = 5
    zero_and_comma = 2
    k = 10
    
    temp_mass = positive.copy()
    for i in range(digits_after_comma+zero_and_comma, zero_and_comma-1, -1):
        
        digit_mass = [0] * k
        for j in range(len(positive)):
            d = digit(positive[j],i)
            digit_mass[d] += 1

        count = 0
        for j in range(k):
            tmp = digit_mass[j]
            digit_mass[j] = count
            count += tmp

        for j in range(len(positive)):
            d = digit(positive[j],i)
            temp_mass[digit_mass[d]] = positive[j]
            digit_mass[d] += 1

        positive = temp_mass.copy()

    temp_mass = negative.copy()
    for i in range(digits_after_comma+zero_and_comma, zero_and_comma-1, -1):
        digit_mass = [0] * k
        for j in range(len(negative)):
            d = digit(negative[j],i)
            digit_mass[d] += 1

        count = 0
        for j in range(k):
            tmp = digit_mass[j]
            digit_mass[j] = count
            count += tmp

        for j in range(len(negative)):
            d = digit(negative[j],i)
            temp_mass[digit_mass[d]] = negative[j]
            digit_mass[d] += 1

        negative = temp_mass.copy()
        
    return list(reversed(negative))+positive

print("\nОтсортированный массив:\n{}".format(least_significant_digit_sort(data_array)))