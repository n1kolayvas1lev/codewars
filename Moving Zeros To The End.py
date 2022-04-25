# Write an algorithm that takes an array
# and moves all of the zeros to the end,
# preserving the order of the other elements.

def move_zeros(array):
    result = []
    zero_counter = []
    for i in range(len(array)):
        if array[i] != 0:
            result.append(array[i])
        else:
            zero_counter.append(array[i])
    array = result + zero_counter
    print(array)


if __name__ == '__main__':
    move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
    move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
    move_zeros([0, 0])
    move_zeros([0])
    move_zeros([])
