class Node: 

    def __init__(self,item = 0): 
        self.key = item 
        self.left,self.right = None,None

root = Node() 
#root = None

def insertRec(root, key): 

    if (root == None): 
        root = Node(key) 
        return root 

    if (key < root.key): 
        root.left = insertRec(root.left, key) 
    elif (key > root.key): 
        root.right = insertRec(root.right, key) 
 
    return root 

def inorderRec(root): 
     if (root != None): 
        inorderRec(root.left) 
        print(root.key ,end = " ") 
        inorderRec(root.right) 

def treeins(arr): 
    for i in range(len(arr)): 
        global root 
        root = insertRec(root, arr[i])
        if i == 0:
            save_root = root
    return save_root 

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        key = arr[0]
        arr_left = []
        arr_right = []

        for i in range(1, len(arr)):
            if arr[i] < key or arr[i] == key:
                arr_left.append(arr[i])
            else:
                arr_right.append(arr[i])

        return quick_sort(arr_left) + [key] + quick_sort(arr_right)
    
def selection_sort(arr):
    n = len(arr)
    while n > 2:
        max = 0
        i_max = 0
        for i in range(n):
            if abs(arr[i]) > abs(max):
                max = arr[i]
                i_max = i
        arr[i_max], arr[n-1] = arr[n-1], arr[i_max]
        n -= 1
    return arr
    
def shaker_sort(arr): 
    n = len(arr) 
    left = 0 
    right = n - 1 
    while left <= right: 
        for i in range(left, right): 
            if arr[i] > arr[i + 1]: 
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
        right -= 1 
        for i in range(right, left, -1): 
            if arr[i - 1] > arr[i]: 
                arr[i], arr[i - 1] = arr[i - 1], arr[i] 
        left += 1 
    return arr