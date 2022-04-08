# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)

def solution(input_string: str) -> str:
    exit_string = ''
    for i in range(len(input_string)):
        if input_string[i] != input_string[i].upper():
            exit_string += input_string[i]
        else:
            exit_string += ' '
            exit_string += input_string[i]

    return exit_string


if __name__ == '__main__':
    solution("helloWorld")
    solution("camelCase")
    solution("breakCamelCase")

