import numpy as np

# np.set_printoptions(threshold=1000000)
float_formatter = "{:.5f}".format
np.set_printoptions(formatter={'float_kind': float_formatter})
# создание матрицы коэфицентов

coefficients = np.zeros((100, 100))
coefficients[0] = np.ones((1, 100))
for stroka in range(1, 99):
    coefficients[stroka][stroka - 1] = 1
    coefficients[stroka][stroka] = 10
    coefficients[stroka][stroka + 1] = 1
coefficients[99][98] = 1
coefficients[99][99] = 1

# создание столбца чисел из правой части
F = np.zeros((100, 1))
for i in range(100):
    F[i][0] = 100 - i

# получение нулей под главной диагональю и соответсвующее изменение  столбца F
# i обходит все строки
# j обходит строки от i-ой до конца, получаем нули под coefficients[i][i]
for i in range(100):
    for j in range(i + 1, 100):
        if coefficients[j][i] != 0:
            new_stroka = ((coefficients[i] * coefficients[j][i]) / coefficients[i][i]) - coefficients[j]
            new_f = ((F[i][0] * coefficients[j][i]) / coefficients[i][i]) - F[j][0]

            coefficients[j] = new_stroka
            F[j][0] = new_f
# в список Х будем добавлять найденные иксы начиная с последнего
x_vector1 = np.zeros((100, 1))

for i in range(100)[::-1]:
    vychet = 0
    for j in range(100):
        if i != j:
            vychet = vychet - coefficients[i][j] * x_vector1[j][0]
    x_vector1[i][0] = (F[i][0] + vychet) / coefficients[i][i]

# для проверки выведем сумму всех х, которая должна равняться 100 по условию
print("проверка решения прямым методом Гауса (ожидаемое значение 100) :", sum(x_vector1)[0])

# заново создадим маьрицу коэфицентов и F
coefficients = np.zeros((100, 100))
coefficients[0] = np.ones((1, 100))
for stroka in range(1, 99):
    coefficients[stroka][stroka - 1] = 1
    coefficients[stroka][stroka] = 10
    coefficients[stroka][stroka + 1] = 1
coefficients[99][98] = 1
coefficients[99][99] = 1

for i in range(100):
    F[i][0] = 100 - i

# норма вектора невязки для метода гауса
print("Норма вектора невязки для метода гауса", np.linalg.norm(F - np.dot(coefficients, x_vector1)))

#  произвольно выберем столбец Х в котором все будут 1
x_vector2 = np.zeros((100, 1))
for i in range(100):
    x_vector2[i][0] = 1

eps = 10 ** -12
# будем проделывать итеррации пока не приблизимся к ответу с заданной точностью
while (np.linalg.norm(np.dot(coefficients, x_vector2) - F)) > eps:
    for i in range(100):
        vychet = 0
        for j in range(100):
            if i != j:
                vychet = vychet - coefficients[i][j] * x_vector2[j][0]
        x_vector2[i][0] = (F[i][0] + vychet) / coefficients[i][i]

# для проверки выведем сумму всех х, которая должна равняться 100 по условию
print("проверка решения прямым методом Якоби(ожидаемое значение 100) :", sum(x_vector2)[0])

# норма вектора невязки для метода Якоби
print("Норма вектора невязки для метода Якоби", np.linalg.norm(F - np.dot(coefficients, x_vector2)))

# минимальные и максимальные собственные числа
print("λ max=", max((np.linalg.eig(coefficients))[0]))
print("λ min=", min((np.linalg.eig(coefficients))[0]))

print("Число обусловленности: ", np.linalg.norm(coefficients) * np.linalg.norm(np.linalg.inv(coefficients)))
