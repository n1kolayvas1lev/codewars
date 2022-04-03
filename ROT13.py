# ROT13 is a simple letter substitution cipher
# that replaces a letter with the letter 13 letters after it in the alphabet.
# ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string,
# they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted,
# like in the original Rot13 "implementation".
def rot13(message):
    alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    exit_ = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i] in alpha_upper:
                for point in range(len(alpha_upper)):
                    if message[i] == alpha_upper[point]:
                        if point + 13 >= len(alpha_upper):
                            exit_ += alpha_upper[point + 13 - len(alpha_upper)]
                        else:
                            exit_ += alpha_upper[point + 13]
            elif message[i] in alpha_lower:
                for point in range(len(alpha_lower)):
                    if message[i] == alpha_lower[point]:
                        if point + 13 >= len(alpha_lower):
                            exit_ += alpha_lower[point + 13 - len(alpha_lower)]
                        else:
                            exit_ += alpha_lower[point + 13]
            else:
                exit_ += message[i]
        else:
            exit_ += message[i]
    return exit_



if __name__ == '__main__':

    print(rot13("a."))
