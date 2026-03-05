def ft_harvest_total():
    harvest_day_one = int(input("Day 1 harvest: "))
    harvest_day_two = int(input("Day 2 harvest: "))
    harvest_day_three = int(input("Day 3 harvest: "))
    harvest_days_total = harvest_day_one + harvest_day_two + harvest_day_three
    print(f"Total harvest: {harvest_days_total}")
