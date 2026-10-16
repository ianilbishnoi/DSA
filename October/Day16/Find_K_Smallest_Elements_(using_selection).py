def kSmallest(arr, k):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr[:k]


#arr=[1,2,3,4,5] , k =3
#arr[start:end:step] 
#arr[:k] = [1,2,3]
      
  
  
