class insertionSort():
    def __init__(self,arr):
        self.arr = arr
        print(arr)

    def insert(self):
        for i in range(1, len(arr)):
            j = i
            while (j > 0 and arr[j] < arr[j - 1]):
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                j = j - 1
        print(arr)





# a = insertionSort

arr = [33,46,59,20,71,18,44,25,11,78]
a = insertionSort(arr)
a.insert()




