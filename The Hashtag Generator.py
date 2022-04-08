# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# Here's the deal:
#     It must start with a hashtag (#).
#     All words must have their first letter capitalized.
#     If the final result is longer than 140 chars it must return false.
#     If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

# def generate_hashtag(s):
#     output = "#"
#
#     for word in s.split():
#         output += word.capitalize()
#
#     return False if (len(s) == 0 or len(output) > 140) else output


def generate_hashtag(incoming_string):
    outcoming_string = []
    if len(incoming_string) == 0:
        return False
    else:
        incoming_string = list(incoming_string.split(' '))
        for i in range(len(incoming_string)):
            if incoming_string[i] != ' ' and len(incoming_string[i]) > 0:
                outcoming_string.append(incoming_string[i])
        for i in range(len(outcoming_string)):
            outcoming_string[i] = outcoming_string[i].capitalize()
        outcoming_string.insert(0, '#')
        outcoming_string = ''.join(i for i in outcoming_string)
    if len(outcoming_string) <= 140:
        return outcoming_string
    else:
        return False


if __name__ == '__main__':
    generate_hashtag('')
    generate_hashtag('Do We have A Hashtag')
    generate_hashtag('Codewars')
    generate_hashtag('Codewars      ')
    generate_hashtag('Codewars Is Nice')
    generate_hashtag('codewars is nice')
    generate_hashtag('CodeWars is nice')
    generate_hashtag('c i n')
    generate_hashtag('codewars  is  nice')
    generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat')
