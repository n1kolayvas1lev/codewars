def format_duration(seconds):
    result = ''
    intermediate_result = {'years': 0, 'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}
    dividers = {'years': 31536000, 'days': 86400, 'hours': 3600, 'minutes': 60, 'seconds': 1}
    if seconds > 0:
        for i in dividers:
            difference = seconds // dividers[i]
            if difference >= 1:
                intermediate_result[i] = difference
                seconds -= dividers[i] * difference
    else:
        result = 'now'

    for i in intermediate_result:
        if i != 'seconds' and i != 'minutes':
            if intermediate_result[i] == 1:
                result += f' {intermediate_result[i]} {i[:-1]},'
            elif intermediate_result[i] > 1:
                result += f' {intermediate_result[i]} {i},'
        elif i == 'minutes':
            if intermediate_result[i] == 1:
                result += f' {intermediate_result[i]} {i[:-1]}'
            elif intermediate_result[i] > 1:
                result += f' {intermediate_result[i]} {i}'
        else:
            if len(result) > 0:
                if intermediate_result[i] == 1:
                    result += f' and {intermediate_result[i]} {i[:-1]}'
                elif intermediate_result[i] > 1:
                    result += f' and {intermediate_result[i]} {i}'
            else:
                if intermediate_result[i] == 1:
                    result += f'{intermediate_result[i]} {i[:-1]}'
                elif intermediate_result[i] > 1:
                    result += f'{intermediate_result[i]} {i}'
    result = result.rstrip(',')
    print(result.strip())


if __name__ == '__main__':
    format_duration(15731080)
