def bubble_sort(array):

    swapped = True
    end = len(array) - 1

    while swapped:
        swapped = False

        for i in range(end):
            current_num = array[i]
            next_num = array[i + 1]

            if current_num > next_num:
                temp = current_num
                array[i] = next_num
                array[i + 1] = temp

                swapped = True

            end -= 1




numbers = [29, 10, 14, 37, 13, 5, 22]

bubble_sort(numbers)

print(numbers)