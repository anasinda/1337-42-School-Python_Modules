def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_check = seed_type.capitalize()

    if unit == "packets":
        print(f"{seed_check} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_check} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_check} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
