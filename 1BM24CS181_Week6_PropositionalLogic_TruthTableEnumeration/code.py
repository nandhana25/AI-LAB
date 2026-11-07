from itertools import product

def implies(a, b):
    return not a or b

def check_kb(p, q, r):
    return implies(q, p) and implies(p, not q) and (q or r)

print("P Q R | Q->P P->~Q Q|R | KB")

for p, q, r in product([False, True], repeat=3):
    c1 = implies(q, p)
    c2 = implies(p, not q)
    c3 = q or r
    kb = c1 and c2 and c3

    print(int(p), int(q), int(r), "|",
          int(c1), int(c2), int(c3), "|", int(kb))

queries = {
    "R": lambda p, q, r: r,
    "R -> P": lambda p, q, r: implies(r, p),
    "Q -> R": lambda p, q, r: implies(q, r)
}

print("\nEntailment Results:")

for name, query in queries.items():
    entailed = True

    for p, q, r in product([False, True], repeat=3):
        if check_kb(p, q, r) and not query(p, q, r):
            entailed = False
            break

    print(name, ":", "Entailed" if entailed else "Not Entailed")
