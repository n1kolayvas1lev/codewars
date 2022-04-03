# Your task is to sort a given string. Each word in the string will contain a single number.
# This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.
# Examples
#
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""
def order(sentence: str) -> str:
    output_str = ''
    if len(sentence) > 0:
        order_ = sentence.split(' ')
        new_order = {}
        for i in order_:
            for num in i:
                if num.isdigit():
                    num = int(num)
                    new_order[num] = i
        for i in range(len(new_order)):
            output_str += new_order[i + 1]
            output_str += ' '
    output_str.strip()
    return output_str



if __name__ == '__main__':
    print(order("is2 Thi1s T4est 3a"))
    print(order("4of Fo1r pe6ople g3ood th5e the2"))