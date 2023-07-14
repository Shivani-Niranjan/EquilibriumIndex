def equilibriumIndex(array):
    count = 0
    for i in range(1, len(array)):
        if (array[i - 1] == (array[len(array) - 1] - array[i])):
            count +=1
    count = (-1 if count == 0 else count)
    return count


def prefixSum(array):
    for i in range(1,len(array)):
        array[i] += array[i-1]
    return array

array = list(map(int,input().split()))
prefixSum(array)
print(array)
print(equilibriumIndex(array))