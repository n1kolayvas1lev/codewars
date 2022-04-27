def format_duration(seconds):
    result = ''
    intermediate_result = []
    dividers = {'years': 31536000, 'days': 86400, 'hours': 3600, 'minutes': 60, 'seconds': 1}
    if seconds > 0:
        for i in dividers:
            difference = seconds // dividers[i]
            if difference >= 1:
                intermediate_result.append((difference, i))
                seconds -= dividers[i] * difference
    else:
        result = 'now'
    for i in range(len(intermediate_result)):
        string = intermediate_result[i][1]
        number = intermediate_result[i][0]
        if i < len(intermediate_result) - 2 or len(intermediate_result) == 1:
            if number > 1:
                result += f' {number} {string},'
            else:
                result += f' {number} {string[:-1]},'
        elif i == len(intermediate_result) - 2:
            if number > 1:
                result += f' {number} {string}'
            else:
                result += f' {number} {string[:-1]}'
        else:
            if number > 1:
                result += f' and {number} {string}'
            else:
                result += f' and {number} {string[:-1]}'

    return result.strip().rstrip(',')


if __name__ == '__main__':
    format_duration(15731080)
    format_duration(1)
    format_duration(62)
    format_duration(120)
    format_duration(3600)
    format_duration(3662)
    format_duration(31626060)
    format_duration(0)
