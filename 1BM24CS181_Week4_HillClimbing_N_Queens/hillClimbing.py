def calculate_cost(state):
    cost = 0

    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


def generate_neighbors(state):
    neighbors = []

    for i in range(4):
        for j in range(i + 1, 4):
            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(new_state)

    return neighbors


def hill_climbing(state):
    while True:
        current_cost = calculate_cost(state)

        if current_cost == 0:
            return state

        neighbors = generate_neighbors(state)

        best_state = min(neighbors, key=calculate_cost)
        best_cost = calculate_cost(best_state)

        if best_cost >= current_cost:
            return state

        state = best_state


def display_board(state):
    print("\nFinal Chessboard:")

    for row in range(4):
        for col in range(4):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" - ", end="")
        print()



initial_state = [3, 1, 2, 0]

final_state = hill_climbing(initial_state)

print("Final State:", final_state)
print("Final Cost:", calculate_cost(final_state))

if calculate_cost(final_state) == 0:
    print("Solution Found!")
    display_board(final_state)
else:
    print("Solution Not Found!")
