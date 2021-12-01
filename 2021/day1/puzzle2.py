def main():
    measurements = []
    input = open("2021/day1/input.txt", "r") 
    #input = open("2021/day1/testdata.txt", "r") 
    for line in input.readlines():
        measurements.append(line)
    input.close()

    increases = 0
    for idx, val in enumerate(measurements):
        if idx < 3:
            continue
        else:
            first = int(measurements[idx-3])
            second = int(measurements[idx-2])
            third = int(measurements[idx-1])
            fourth = int(measurements[idx])

            a = first + second + third
            b = second + third + fourth
            print(a, b)

            if b > a:
                increases += 1

    print(f"increases: {increases}")

if __name__ == '__main__':
    main()