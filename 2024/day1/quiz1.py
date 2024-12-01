with open("2024/day1/quiz1_input.txt", "r") as f:
    left_values = []
    right_values = []
    for line in f:
        columns = line.split()
        left = columns[0]
        right = columns[1]
        left_values.append(left)
        right_values.append(right)
    left_values = sorted(left_values)
    right_values = sorted(right_values)

    distances = []
    for idx in range(max(len(left_values), len(right_values))):
        left = left_values[idx]
        right = right_values[idx]
        distance = abs(int(left) - int(right))
        distances.append(distance)

    print(sum(distances))