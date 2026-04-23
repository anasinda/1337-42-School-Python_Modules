class Plants:
    def __init__(self, name: str, height_cm: int, age_days: int):
        """Setting up plant attributes"""
        self.name = name
        self.height = height_cm
        self.age = age_days

    def grow_plant(self) -> None:
        """Grow plant by 1cm per call"""
        self.height += 1

    def age_plant(self) -> None:
        """Plant is aged by 1 day per call"""
        self.age += 1

    def get_info(self, growth_from: int) -> None:
        """Gets plant details from a set period to another"""
        print(f"=== Day {growth_from} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        if growth_from > 1:
            print(f"Growth this week: +{growth_from - 1}cm")


rose = Plants("Rose", 25, 30)
sun_flower = Plants("Sunflower", 80, 45)
cactus = Plants("Cactus", 15, 120)


def age_plants(plant: Plants, growth_from: int, growth_to: int) -> None:
    """Plant aging function deping from when till what"""
    plant.get_info(growth_from)
    while growth_from < growth_to:
        plant.grow_plant()
        plant.age_plant()
        growth_from += 1
    plant.get_info(growth_from)


age_plants(rose, 1, 7)
