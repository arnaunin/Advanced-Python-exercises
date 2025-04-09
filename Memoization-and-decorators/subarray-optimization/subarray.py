import functools

@functools.lru_cache(maxsize=None)
def max_sub_array_sum(arr):
    if not arr:
        return 0
    
    current_sum = max_sum = arr[0]
    current_subarray = max_subarray = [arr[0]]

    for num in arr[1:]:
        if num > current_sum+num:
            current_sum = num
            max_subarray = [num]
        else:
            current_sum += num
            current_subarray.append(num)

        if current_sum > max_sum:
            max_sum = current_sum
            max_subarray = current_subarray.copy()

    return max_sum, max_subarray

array = tuple([1, -2, 3, 10, -4, 7, 2, -5, -2])
resultado, subarray = max_sub_array_sum(array)
print("Maximum sum of contiguous subarray:", resultado)
print("Contiguous subarray with maximum sum:", subarray)