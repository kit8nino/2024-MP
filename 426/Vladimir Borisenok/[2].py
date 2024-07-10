import random
import math
import re

numbers = [i for i in range(999999)]
random.shuffle(numbers)


rnumbers = [random.uniform(-1, 1) for _ in range(99999)]

day = 29
month = 8
radius = day / month 

complexpoints = []

while len(complexpoints) < 42000:
    x = random.uniform(-radius, radius) 
    yr = math.sqrt(radius**2 - x**2) 
    y = random.uniform(-yr, yr)
    
    point = complex(x, y)
    complexpoints.append(point)

book = 'book.txt'
with open(book, 'r', encoding='utf-8') as file:
    text = file.read()
    wordlist = re.findall(r'\b[A-Za-z]+\b', text)
    
    
def shaker(numbers):
    left = 0
    right = len(numbers) - 1
    swap = True
    
    while left < right and swap:
        swap = False
        
        for i in range(left, right): #Идем справа налево
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swap = True
                
        right -= 1
        
        if not swap: 
            break
            
        for i in range(right, left, -1): #Идем слева направо
            if numbers [i] < numbers[i-1]:
                numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
                swap = True
        left +=1
    return numbers

sorted_numbers = shaker(numbers)
print("Отсортированные числа: ", sorted_numbers)


def selection(rnumbers):
    n = len(rnumbers)
    
    for i in range(n): 
        mini = i
        
        for j in range(i+1, n): 
            if rnumbers[j] < rnumbers[mini]:
                mini = j
                
        rnumbers[i], rnumbers[mini] = rnumbers[mini], rnumbers[i] 
        
    return rnumbers

sorted_rnumbers = selection(rnumbers)
print("Отсортированные вещественные числа: ", sorted_rnumbers)


def quicksort(points):
    pivot = points[len(points) // 2] 
    le, eq, gr = [], [], [] 
    
    for point in points:
        if abs(point) < abs(pivot):
            le.append(point)
        elif abs(point) == abs(pivot): 
            eq.append(point)
        else:
            gr.append(point)
    
    return quicksort(le) + eq + quicksort(gr) if le and gr else le + eq + gr 

sorted_complex_numbers = quicksort(complexpoints)
print("Отсортированные комплексные точки: ", sorted_complex_numbers )

def least_sd(words):
    max_len = max(len(word) for word in words)
    
    for i in range(max_len -1, -1, -1):
        buckets = [[] for k in range(256)]
        
        for word in words:
            if i < len(word):
                letter = ord(word[i])
                buckets[letter].append(word)
            else:
                buckets[0].append(word)
                
        word_list = []
        for bucket in buckets:
            word_list.extend(bucket)
            
    return word_list

sorted_words = least_sd(wordlist)
print("Отсортированные слова: ")
for word in sorted_words:
    print(word)
