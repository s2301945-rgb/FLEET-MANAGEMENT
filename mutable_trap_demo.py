class BuggyCart:
    items = []  # shared by every instance — this is the bug

    def __init__(self, owner):
        self.owner = owner


def demonstrate_bug():
    cart_a = BuggyCart("Alice")
    cart_b = BuggyCart("Bob")
    cart_a.items.append("apple")
    print("cart_a.items:", cart_a.items)
    print("cart_b.items:", cart_b.items)
    print("Same list object?", cart_a.items is cart_b.items)


class FixedCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []  # created fresh per instance — this is the fix

    def __str__(self):
        return f"{self.owner}'s cart: {self.items}"


def demonstrate_fix():
    cart_a = FixedCart("Alice")
    cart_b = FixedCart("Bob")
    cart_a.items.append("apple")
    print("cart_a.items:", cart_a.items)
    print("cart_b.items:", cart_b.items)
    print("Same list object?", cart_a.items is cart_b.items)


if __name__ == "__main__":
    print("=== Buggy version ===")
    demonstrate_bug()
    print()
    print("=== Fixed version ===")
    demonstrate_fix()