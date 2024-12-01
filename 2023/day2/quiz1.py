import re

with open("2023/day2/quiz1_input_test.txt", "r") as f:

    pattern = re.compile(r"(\d) (red|blue|green)")
    max_red = 12
    max_green = 13
    max_blue = 14

    for line in f.readlines():
        game_id = line.split(":")[0].split(" ")[1].strip()
        games = line.split(":")[1].strip()
        num_games = games.split(";")
        print(f"Game ID: {game_id}, Number of Games: {len(num_games)}")

        matches = pattern.findall(games)
        for match in matches:
            print(match)

