import random
data_array=[i for i in range(1000000)]
random.shuffle(data_array)
print("Исходный массив:\n{}".format(data_array))

def sort_Shell(data_array):
    d_array=data_array
    array_length=len(d_array)
    step=array_length//2
    while step>0:
        for i in range(step, array_length):
            j=i
            delta = j - step
            while delta >= 0 and d_array[delta] > d_array[j]:
                d_array[j],d_array[delta]=d_array[delta],d_array[j]
                j=delta
                delta=j-step
        step//=2
    return d_array

print("\nОтсортированный массив:\n{}".format(sort_Shell(data_array)))