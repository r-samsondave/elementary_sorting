def bubble_sort(array):

    swapped = True # tracks if a swap happened
    end = len(array) - 1
    number_of_swaps = 0

    while swapped:
        swapped = False # reset the flag in the beginning of each pass

        for i in range(end): # checks adjacent num
            current_num = array[i]
            next_num = array[i + 1]

            if current_num > next_num: # if left value is bigger, swap them
                number_of_swaps += 1
                temp = current_num # save left value before the swapping
                array[i] = next_num
                array[i + 1] = temp

                swapped = True # a swap happened, repeat the process

        end -= 1 # skip the number that's in the final position to avoid unnecessary comparing

    return f'bubble sort: {array}, number of swaps: {number_of_swaps}'


# print(bubble_sort([29, 10, 14, 37, 13, 5, 22]))

def selection_sort(array):

    count_of_swaps = 0

    for i in range(len(array) - 1): # remembers the position where we will put the lowest num
        min_index = i

        for j in range(i + 1, len(array)): # search for the lowest num

            if array[j] < array[min_index]: # compare current num against initial lowest num
                min_index = j # stores the index of initial lowest num
                count_of_swaps += 1


        temp = array[i] # stores the i to temporary storage
        array[i] = array[min_index] # place the final lowest num to its final position
        array[min_index] = temp # swaps with the previous position of lowest num

    return f'array: {array}, Count of swaps: {count_of_swaps}'




print(selection_sort([29, 10, 14, 37, 13, 5, 22]))