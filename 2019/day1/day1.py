import math

def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    #lines = [12, 14, 1969, 100756]
    #lines = [100756]
    total_fuel_required = 0
    for line in lines:
        module_weight = int(line)
        module_fuel_required = getFuelRequired(module_weight)
        total_fuel_required= total_fuel_required + module_fuel_required
    f.close()
    print(total_fuel_required)

def getFuelRequired(load: int):
    print("------------")
    print("Calculating fuel for " + str(load))
    fuel = math.floor(load/3)-2
    print("=> " + str(fuel))
    if fuel < 0:
        # Any mass that would require negative fuel should instead be treated as if it requires zero fuel
        print("Done")
        return 0
    else:
        return fuel + getFuelRequired(fuel)

if __name__ == "__main__":
    main()
