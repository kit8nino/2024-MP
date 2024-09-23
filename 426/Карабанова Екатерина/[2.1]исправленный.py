import random

# исходные данные
integer_list = list(range(1000000))
float_list = [random.uniform(-1, 1) for _ in range(99999)]
complex_points = [random.uniform(-1, 1) + random.uniform(-1, 1)*1j for _ in range(42000)]
book_excerpt = 'Платье - это нечто большее, нежели маскарадный костюм. В новой одежде человек становится иным, хотя сразу это не заметно. Тот, кто по-настоящему умеет носить платья, воспринимает что-то от них; как ни странно, платья и люди влияют друг на друга, и это не имеет ничего общего с грубым переодеванием на маскараде. Можно приспособиться к одежде и вместе с тем не потерять своей индивидуальности. Того, кто понимает это, платья не убивают, как большинство женщин, покупающих себе наряды. Как раз наоборот, такого человека платья любят и оберегают. Они помогают ему больше, чем любой духовник, чем неверные друзья и даже чем возлюбленный. Лилиан все это знала. Она знала, что шляпка, которая идет тебе, служит большей моральной опорой, чем целый свод законов. Она знала, что в тончайшем вечернем платье, если оно хорошо сидит, нельзя простудиться, зато легко простудиться в том платье, которое раздражает тебя, или же в том, двойник которого ты на этом же вечере видишь на другой женщине; такие вещи казались Лилиан неопровержимыми, как химические формулы. Но она знала. также, что в моменты тяжелых душевных переживаний платья могут стать либо добрыми друзьями, либо заклятыми врагами; без их помощи женщина чувствует себя совершенно потерянной, зато, когда они помогают ей, как помогают дружеские руки, женщине намного легче в трудный момент. Во всем этом нет ни грана пошлости, просто не надо забывать, какое большое значение имеют в жизни мелочи. Как хорошо, когда освоишь эту науку, - подумала Лилиан. К тому же она была почти единственная, еще доступная ей. У нее не осталось времени для того, чтобы оправдать свою жизнь чем-то большим; у нее не было времени даже для бунта. Бунт, о котором она мечтала когда-то, она уже совершила и теперь по временам начинала сомневаться в своей правоте. Сейчас ей осталось только одно - свести свои счеты с судьбой.'


sorting_algorithms = ['shaker sort', 'bubble sort', 'insertion sort']


def shaker_sort(array):
    # Сортировка перемешиванием
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start += 1


def bubble_sort(array):
    # Сортировка пузырьком
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def insertion_sort(array):
    # Сортировка вставкой
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

for algorithm in sorting_algorithms:
    if algorithm == 'shaker sort':
        shaker_sort(integer_list)
    elif algorithm == 'bubble sort':
        bubble_sort(float_list)
    elif algorithm == 'insertion sort':
        insertion_sort(complex_points)
    elif algorithm == 'timsort':
         float_list.sort()

print("Сортировка integer:", integer_list[:20])
print("Сортировка float:", float_list[:20])
print("Сортировка complex:", complex_points[:20])
print("Сортировка book:", book_excerpt[:20])
