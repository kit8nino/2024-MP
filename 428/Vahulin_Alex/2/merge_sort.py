import codecs

def create_string_list():
    fileObj = codecs.open( "2.txt", "r", "utf_8_sig" )
    text = fileObj.read()
    text = text.replace('–', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace('.', '')
    text = text.replace(':', '')
    text = text.replace('-', '') 
    fileObj.close()
    list_of_string = text.split()
    for i in list_of_string:
        if not i[0].isalpha():
            list_of_string.pop(list_of_string.index(i))
    return list_of_string

def merge_sort(data_array):
    data_array=data_array.copy()
    if len(data_array) > 1:
        middle_index = len(data_array) // 2
        left_half = data_array[:middle_index]
        right_half = data_array[middle_index:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data_array[k] = left_half[i]
                i += 1
            else:
                data_array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data_array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data_array[k] = right_half[j]
            j += 1
            k += 1

data_array = create_string_list()
print("Исходный массив данных:\n{}".format(data_array))

merge_sort(data_array)
print("Отсортированный массив:\n{}",data_array)