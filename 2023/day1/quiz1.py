import re

with open("2023/day1/quiz1_input.txt", "r") as f:
    lines = f.readlines()
    pattern = re.compile(r"\d")
    calibrationValues = []
    for line in lines:
        line = line.replace('\n', '')
        matches = pattern.findall(line)

        c = ""
        a = matches[0]
        if len(matches) > 1:
            b = matches[-1]
            c = a+b
        else:
            c = a+a
        print(f"{line} --> {matches} --> {c}")
        if len(c) != 2:
            print(f"ERROR: {line} --> {matches} --> {c}")
        else:
            print(int(c))
        calibrationValues.append(int(c))
    print(sum(calibrationValues))