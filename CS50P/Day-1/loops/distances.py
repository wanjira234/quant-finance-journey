distances = {
    "Voyager 1": 163,
    "Voyager 2": 228,
    "pioneer 10": 80,
    "New Horizons": 58,
    "pioneer 11": 44,
}

def main():
    # for name in distances.keys():
    #     print(f"{name} is {distances[name]} Au from Earth")
    for distance in distances.values():
        print(f"{distance} Au is {convert(distance)} m")

def convert(au):
    return au * 149597870700

main()