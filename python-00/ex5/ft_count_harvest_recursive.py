def ft_cd_counter(start_count, days_left):
    if start_count > days_left:
        print("Harvest time!")
    else:
        print(f"Day {start_count}")
        ft_cd_counter(start_count + 1, days_left)


def ft_count_harvest_recursive():
    days_left = int(input("Days until harvest: "))
    ft_cd_counter(1, days_left)
