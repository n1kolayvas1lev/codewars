# In this kata you have to create all permutations of a non empty input string
# and remove duplicates, if present.
# This means, you have to shuffle all letters from the input in all possible orders.
# Examples:
# * With input 'a'
# * Your function should return: ['a']
# * With input 'ab'
# * Your function should return ['ab', 'ba']
# * With input 'aabb'
# * Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# The order of the permutations doesn't matter.
from itertools import permutations as pm


def permutations(string: str) -> list:
    mutated = list(pm(string))
    cleaned = []
    result = []
    resulted_str = ''
    for i in mutated:
        if i not in cleaned:
            cleaned.append(i)
    for i in cleaned:
        for char in i:
            resulted_str += ''.join(char)
        result.append(resulted_str)
        resulted_str = ''

    return result


if __name__ == "__main__":
    print(sorted(permutations('a')))
    print(sorted(permutations('ab')))
    print(sorted(permutations('aabb')))
