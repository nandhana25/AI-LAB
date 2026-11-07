
def is_variable(x):
    return isinstance(x, str) and x.islower()

def substitute(term, subst):
    while is_variable(term) and term in subst:
        term = subst[term]

    if isinstance(term, tuple):
        return tuple(substitute(x, subst) for x in term)

    return term

def occurs_check(var, term, subst):
    term = substitute(term, subst)

    if var == term:
        return True

    if isinstance(term, tuple):
        return any(occurs_check(var, x, subst) for x in term)

    return False

def unify(x, y, subst):
    x = substitute(x, subst)
    y = substitute(y, subst)

    if x == y:
        return subst

    if is_variable(x):
        if occurs_check(x, y, subst):
            return None
        subst[x] = y
        return subst

    if is_variable(y):
        if occurs_check(y, x, subst):
            return None
        subst[y] = x
        return subst

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y) or x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)

            if subst is None:
                return None

        return subst

    return None

expr1 = ('Eats', 'x', 'Apple')
expr2 = ('Eats', 'Riya', 'y')

print("Expression 1:", expr1)
print("Expression 2:", expr2)

result = unify(expr1, expr2, {})

if result is not None:
    print("\nUnification Successful")
    print("Substitution Set:", result)
    print("Unified Expression:", substitute(expr1, result))
else:
    print("\nUnification Failed")
