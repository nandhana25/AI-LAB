import random
import math

# Calculate attacking queen pairs
def calculate_cost(state):
    cost = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


# Simulated Annealing Algorithm
def simulated_annealing():

    state = [random.randint(0, 7) for _ in range(8)]

    temperature = 100
    cooling_rate = 0.99
    min_temperature = 0.001

    while temperature > min_temperature:

        current_cost = calculate_cost(state)

        if current_cost == 0:
            return state

        # Generate neighboring state
        new_state = state.copy()
        col = random.randint(0, 7)
        row = random.randint(0, 7)

        new_state[col] = row

        new_cost = calculate_cost(new_state)

        delta = new_cost - current_cost

        # Accept or reject new state
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            state = new_state

        # Reduce temperature
        temperature *= cooling_rate

    return state


# Main Program
solution = None

# Random restarts to improve chances of finding a solution
for _ in range(100):
    solution = simulated_annealing()

    if calculate_cost(solution) == 0:
        break

# Display final result
print("Final State:", solution)
print("Final Cost:", calculate_cost(solution))

if calculate_cost(solution) == 0:
    print("\nSolution Found!")

    for row in range(8):
        for col in range(8):
            if solution[col] == row:
                print(" Q ", end="")
            else:
                print(" - ", end="")
        print()
else:
    print("Solution Not Found!")
