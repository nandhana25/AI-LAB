def vacuum_cleaner():
    room = {
        "A": "Dirty",
        "B": "Dirty"
    }

    position = "A"

    print("Initial State:")
    print(room)
    print("Vacuum Position:", position)

    while "Dirty" in room.values():

       
        if room[position] == "Dirty":
            print("\nRoom", position, "is Dirty")
            print("Action: SUCK")
            room[position] = "Clean"

       
        elif room[position] == "Clean":
            if position == "A":
                print("\nRoom A is Clean")
                print("Action: MOVE RIGHT")
                position = "B"
            else:
                print("\nRoom B is Clean")
                print("Action: MOVE LEFT")
                position = "A"

        print("Current State:", room)
        print("Vacuum Position:", position)

    print("\nBoth rooms are Clean!")
    print("Goal State Reached.")


vacuum_cleaner()
