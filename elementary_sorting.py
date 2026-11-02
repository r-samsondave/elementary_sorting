def bubble_sort(array):

    swapped = True # tracks if a swap happened
    end = len(array) - 1
    swap_count = 0

    while swapped:
        swapped = False # reset the flag in the beginning of each pass

        for i in range(end): # checks adjacent num
            current_num = array[i]
            next_num = array[i + 1]

            if current_num > next_num: # if left value is bigger, swap them
                swap_count += 1
                temp = current_num # save left value before the swapping
                array[i] = next_num
                array[i + 1] = temp

                swapped = True # a swap happened, repeat the process

        end -= 1 # skip the number that's in the final position to avoid unnecessary comparing

    return f'{array}, number of swaps: {swap_count}'

def selection_sort(array):

    swap_count = 0

    for i in range(len(array) - 1): # remembers the position where we will put the lowest num
        min_index = i

        for j in range(i + 1, len(array)): # search for the lowest num

            if array[j] < array[min_index]: # compare current num against initial lowest num
                min_index = j # stores the index of initial lowest num

        if min_index != i:
            temp = array[i] # stores the i to temporary storage
            array[i] = array[min_index] # place the final lowest num to its final position
            array[min_index] = temp # swaps with the previous position of lowest num
            swap_count += 1

    return f'array: {array}, Count of swaps: {swap_count}'


def insertion_sort(array):
    shift_count = 0

    for i in range(1, len(array)): # it identifies the key

        key = array[i] # it preserves the value

        j = i - 1 # position starts before the key

        while j >= 0 and array[j] > key: # make sure that j stays within the array
                                         # it also checks if the value of array[j] is greater than key value

            array[j + 1] = array[j] # shift the greater number to right
            shift_count += 1
            j -= 1 # allows to traverse backward

        array[j + 1] = key # if there's no shifting happen, it will go back to the same place


    return f'{array}, Count of shifts: {shift_count}'

test_cases = {
    "Random": [29, 10, 14, 37, 13, 5, 22],
    "Already sorted": [1, 2, 3, 4, 5, 6, 7],
    "Reverse sorted": [7, 6, 5, 4, 3, 2, 1],
    "Duplicates": [4, 2, 4, 1, 2, 3, 1],
    "Edge cases1": [2, 1],
    "Edge cases2": [],
    "Edge cases3": [2],


}

for name, array in test_cases.items():
    print(f"{name}: {insertion_sort(array)}")