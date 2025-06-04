def main():
    spacecraft = {
        "name": "james webb space TELESCOPE",
        # "distance": 163,
    }
    # adding keys in various ways
    # spacecraft["distance"] = 0.01
    spacecraft.update({'distance': 0.01, 'orbit': "sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f""" 
        ========REPORT========
        Name: {spacecraft["name"]}
        Distance: {spacecraft.get("distance", "unknown")} AU
        Orbit: {spacecraft.get("orbit", "unknown")}

        =======================
    """
main()