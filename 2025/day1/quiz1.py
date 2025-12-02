

def parse_rotations_instr(instr: str) -> int:
    c = int(instr[1:])
    if instr[0] == "L":
        c = c*-1
    return c

def main():
    dial_position = 50
    dial_length = 100
    zero_counter = 0
    if True:
        with open("./2025/day1/quiz1_input.txt", "r", -1, None, None, "") as f:
            rotations = [line.strip() for line in f]
    else:
        rotations = ["L50", "L1", "R20"]
    for rotation in rotations:
        old_position = dial_position
        instr = parse_rotations_instr(rotation)
        new_position = dial_position + instr
        new_position_mod = new_position % dial_length

        laps = 0
        # laps = abs(old_position + instr) // dial_length

        if new_position_mod == 0:
            zero_counter += 1
        # zero_counter += laps
        
        print(f"Old position = {dial_position}, rotation = {instr}, new position = {new_position}, new position (mod): {new_position_mod}, {laps=}, {zero_counter=}")
        dial_position = new_position_mod
    print(zero_counter)


if __name__ == "__main__":
    main()