facts = {
    ("American", "Robert"),
    ("Missile", "T1"),
    ("Owns", "A", "T1"),
    ("Enemy", "A", "America")
}

rules = [
    ("Missile", "Weapon"),
    ("Enemy", "Hostile")
]

query = ("Criminal", "Robert")

def forward_chaining(facts):
    while True:
        new_facts = set()

        for rule in rules:
            source, target = rule

            for fact in facts:
                if fact[0] == source:
                    new_facts.add((target, fact[1]))

        for fact in facts:
            if fact[0] == "Missile":
                missile = fact[1]

                if ("Owns", "A", missile) in facts:
                    new_facts.add(("Sells", "Robert", missile, "A"))

        for fact in facts:
            if fact[0] == "American":
                person = fact[1]

                for weapon in facts:
                    if weapon[0] == "Weapon":
                        item = weapon[1]

                        for sale in facts:
                            if sale == ("Sells", person, item, "A"):
                                if ("Hostile", "A") in facts:
                                    new_facts.add(("Criminal", person))

        new_facts -= facts

        if not new_facts:
            break

        print("New facts inferred:", new_facts)
        facts.update(new_facts)

    return query in facts


print("Initial Facts:", facts)

if forward_chaining(facts):
    print("\nQuery Proved:", query)
else:
    print("\nQuery Not Proved:", query)
