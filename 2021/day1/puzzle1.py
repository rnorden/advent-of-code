def main():
    measurements = []
    input = open("2021/day1/input.txt", "r") 
    #input = open("2021/day1/testdata.txt", "r") 
    for line in input.readlines():
        measurements.append(line)
    input.close()

    increases = 0
    for idx, val in enumerate(measurements):
        if int(val) > int(measurements[idx-1]):
            increases += 1

    print(increases)

if __name__ == "__main__":
    main()