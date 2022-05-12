# Radix Sort Complexity
# Time Complexity	 
# Best	O(n+k)
# Worst	O(n+k)
# Average	O(n+k)
# Space Complexity	O(max)
# Stability	Yes
# Since radix sort is a non-comparative algorithm, it has advantages over comparative sorting algorithms.

# For the radix sort that uses counting sort as an intermediate stable sort, the time complexity is O(d(n+k)).

# Here, d is the number cycle and O(n+k) is the time complexity of counting sort.

# Thus, radix sort has linear time complexity which is better than O(nlog n) of comparative sorting algorithms.

# If we take very large digit numbers or the number of other bases like 32-bit and 64-bit numbers then it can perform in linear time however the intermediate sort takes large space.

# This makes radix sort space inefficient. This is the reason why this sort is not used in software libraries.

# Radix Sort Applications
# Radix sort is implemented in

# DC3 algorithm (Kärkkäinen-Sanders-Burkhardt) while making a suffix array.
# places where there are numbers in large ranges.


# PSEUDO

# radixSort(array)
#   d <- maximum number of digits in the largest element
#   create d buckets of size 0-9
#   for i <- 0 to d
#     sort the elements according to ith place digits using countingSort

# countingSort(array, d)
#   max <- find largest element among dth place elements
#   initialize count array with all zeros
#   for j <- 0 to size
#     find the total count of each unique digit in dth place of elements and
#     store the count at jth index in count array
#   for i <- 1 to max
#     find the cumulative sum and store it in count array itself
#   for j <- size down to 1
#     restore the elements to array
#     decrease count of each element restored by 1

# Radix sort in Python


# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)