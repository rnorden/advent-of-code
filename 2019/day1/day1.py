import math

def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    #lines = [12, 14, 1969, 100756]
    total_fuel_required = 0
    for line in lines:
        module_weight = int(line)
        module_fuel_required = math.floor(module_weight/3)-2
        total_fuel_required= total_fuel_required + module_fuel_required
    f.close()
    print(total_fuel_required)

if __name__ == "__main__":
    main()

