def ft_count_harvest_iterative():
    harvest_cd = int(input("Days until harvest: "))
    for i in range(1, harvest_cd + 1, 1):
        print(f"Day {i}")
    print("Harvest time!")
