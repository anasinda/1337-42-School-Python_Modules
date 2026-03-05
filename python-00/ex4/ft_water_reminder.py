def ft_water_reminder():
    water_check = int(input("Days since last watering: "))
    if water_check > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
