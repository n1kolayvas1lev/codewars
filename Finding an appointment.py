def get_start_time(schedules: list, duration: int) -> str | None:
    duration /= 60
    first_guy_starts = list(schedules[0][i][0] for i in range(len(schedules[0])))
    first_guy_ends = list(schedules[0][i][1] for i in range(len(schedules[0])))
    second_guy_starts = list(schedules[1][i][0] for i in range(len(schedules[1])))
    second_guy_ends = list(schedules[1][i][1] for i in range(len(schedules[1])))
    third_guy_starts = list(schedules[2][i][0] for i in range(len(schedules[2])))
    third_guy_ends = list(schedules[2][i][1] for i in range(len(schedules[2])))

    first_guy_starts = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in first_guy_starts)
    first_guy_ends = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in first_guy_ends)
    second_guy_starts = list(
        int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in second_guy_starts)
    second_guy_ends = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in second_guy_ends)
    third_guy_starts = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in third_guy_starts)
    third_guy_ends = list(int(i[0]) * 10 + int(i[1]) + (int(i[-2]) * 10 + int(i[-1])) / 60 for i in third_guy_ends)
    if len(second_guy_starts) < len(first_guy_starts):
        second_guy_starts.append(19.0)
    if len(second_guy_starts) < len(first_guy_starts):
        second_guy_ends.append(19.0)
    if len(third_guy_starts) < len(first_guy_starts):
        third_guy_starts.append(19.0)
    if len(third_guy_starts) < len(first_guy_starts):
        third_guy_starts.append(19.0)
    available_starts = []
    if first_guy_starts[0] >= 9.0 + duration and second_guy_starts[0] >= 9.0 + duration and third_guy_starts[0] >= 9.0 + duration:
        available_starts.append(9.0)
    for i in range(len(first_guy_starts) - 1):
        first = first_guy_starts[i + 1] - first_guy_ends[i]
        second = second_guy_starts[i + 1] - second_guy_ends[i]
        third = third_guy_starts[i + 1] - third_guy_ends[i]
        delta = min(first_guy_starts[i + 1], second_guy_starts[i + 1], third_guy_starts[i + 1]) - max(first_guy_ends[i], second_guy_ends[i], third_guy_ends[i])
        if first >= duration and second >= duration and third >= duration and delta >= duration:
            available_starts.append(max(first_guy_ends[i], second_guy_ends[i], third_guy_ends[i]))
    if len(available_starts) > 0:
        return f'{int(available_starts[0] // 1)}:{int((available_starts[0] % 1) * 60)}'
    else:
        return None


if __name__ == '__main__':
    print(get_start_time([
        [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
        [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
        [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
    ], 60))
