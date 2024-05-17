from filling_arr import filling_arrays
import sort_methods

def main():

    million_list = []
    random_list = []
    complex_list = []
    text_list = []

    filling_arrays(million_list, random_list, complex_list, text_list)

    #random.sample(range(1, 18), 4) #6, 10, 9, 1

    root = sort_methods.treeins(million_list)
    sort_methods.inorderRec(root)

    random_list_sort = sort_methods.quick_sort(random_list)
    for num in random_list_sort:
        print(num)

    complex_list_sort = sort_methods.selection_sort(complex_list)
    for complex_num in complex_list_sort:
        print(complex_num)

    text_list_sort = sort_methods.shaker_sort(text_list)
    for word in text_list_sort:
        print(word)

main()
