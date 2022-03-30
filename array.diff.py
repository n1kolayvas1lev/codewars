# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]
def array_diff(a: list, b: list) -> list:
    exit_ = []
    for i in a:
        if i not in b:
            exit_.append(i)
    return exit_
