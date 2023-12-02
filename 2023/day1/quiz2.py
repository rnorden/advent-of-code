import re

digitPattern = re.compile(r"\d")
pattern = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)")
number_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def optionalConvertSpelledNumber(n):
    if digitPattern.match(n):
        a = n
    else:
        a = number_map[n]
    return a

def firstElementFromNumericKeyMap(numeric_key_map):
    return numeric_key_map[sorted(list(numeric_key_map.keys()))[0]]

def lastElementFromNumericKeyMap(numeric_key_map):
    return numeric_key_map[sorted(list(numeric_key_map.keys()))[-1]]

with open("2023/day1/quiz1_input.txt", "r") as f:
    lines = f.readlines()
    
    calibrationValues = []
    for line in lines:
        line = line.replace('\n', '')
        start_idx = 0

        matches_at_start_idx = {}
        while True:
            #print(f"{start_idx} --> {line[start_idx:]}")
            matches = pattern.match(line[start_idx:])
            if matches: matches_at_start_idx[start_idx] = matches
            if start_idx == len(line) - 1:
                break
            start_idx = start_idx + 1

        print(matches_at_start_idx)
        c = ""
        a = optionalConvertSpelledNumber(firstElementFromNumericKeyMap(matches_at_start_idx).group(0))
        if len(matches_at_start_idx) > 1:
            b = optionalConvertSpelledNumber(lastElementFromNumericKeyMap(matches_at_start_idx).group(0))
            c = a+b
        else:
            c = a+a
        print(f"{line} --> {matches_at_start_idx} --> {c}")
        calibrationValues.append(int(c))
    print(sum(calibrationValues))