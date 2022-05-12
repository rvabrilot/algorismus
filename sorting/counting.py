# countingSort(array, size)
#   max <- find largest element in array
#   initialize count array with all zeros
#   for j <- 0 to size
#     find the total count of each unique element and 
#     store the count at jth index in count array
#   for i <- 1 to max
#     find the cumulative sum and store it in count array itself
#   for j <- size down to 1
#     restore the elements to array
#     decrease count of each element restored by 1

# # Counting sort in Python programming
# Complexity
# Time Complexity	 
# Best	O(n+k)
# Worst	O(n+k)
# Average	O(n+k)
# Space Complexity	O(max)
# Stability	Yes
# Time Complexities

# There are mainly four main loops. (Finding the greatest value can be done outside the function.)

# for-loop	time of counting
# 1st	O(max)
# 2nd	O(size)
# 3rd	O(max)
# 4th	O(size)
# Overall complexity = O(max)+O(size)+O(max)+O(size) = O(max+size)

# Worst Case Complexity: O(n+k)
# Best Case Complexity: O(n+k)
# Average Case Complexity: O(n+k)
# In all the above cases, the complexity is the same because no matter how the elements are placed in the array, the algorithm goes through n+k times.

# There is no comparison between any elements, so it is better than comparison based sorting techniques. But, it is bad if the integers are very large because the array of that size should be made.

# Space Complexity

# The space complexity of Counting Sort is O(max). Larger the range of elements, larger is the space complexity.

# Counting Sort Applications
# Counting sort is used when:

# there are smaller integers with multiple counts.
# linear complexity is the need.

def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)