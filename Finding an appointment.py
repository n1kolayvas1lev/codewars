def get_start_time(schedules: list, duration: int) -> str:
    duration /= 60
    first_guy_starts = (schedules[0][0][0], schedules[0][1][0], schedules[0][2][0], schedules[0][3][0])
    first_guy_ends = (schedules[0][0][1], schedules[0][1][1], schedules[0][2][1], schedules[0][3][1])
    second_guy_starts = (schedules[1][0][0], schedules[1][1][0], schedules[1][2][0])
    second_guy_ends = (schedules[1][0][1], schedules[1][1][1], schedules[1][2][1])
    third_guy_starts = (schedules[2][0][0], schedules[2][1][0], schedules[2][2][0])
    third_guy_ends = (schedules[2][0][1], schedules[2][1][1], schedules[2][2][1])

    first_guy_starts = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in first_guy_starts)
    first_guy_ends = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in first_guy_ends)
    second_guy_starts = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in second_guy_starts)
    second_guy_ends = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in second_guy_ends)
    third_guy_starts = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in third_guy_starts)
    third_guy_ends = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in third_guy_ends)
    available_starts = []
    if first_guy_starts[0] >= 10 and second_guy_starts[0] >= 10 and third_guy_starts[0] >= 10:
        available_starts.append(9.0)
    for i in range(len(first_guy_starts) - 1):
        if first_guy_starts[i + 1] - first_guy_ends[i] >= duration and second_guy_starts[i + 1] - second_guy_ends[i] >= duration and third_guy_starts[i + 1] - third_guy_ends[i] >= duration:
            available_starts.append(max(first_guy_ends[i], second_guy_ends[i], third_guy_ends[i]))
    return f'{int(available_starts[0] // 1)}:{int((available_starts[0] % 1) * 60)}'


if __name__ == '__main__':
    print(get_start_time([
                    [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
                    [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
                    [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
                    ], 60))
