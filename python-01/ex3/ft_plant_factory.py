class Plants:
    count: int = 0

    def __init__(self, name: str, height_cm: int, age_days: int):
        """Setting up plant attributes"""
        """Counting number of plants each time an instance is created"""
        self.name = name
        self.height = height_cm
        self.age = age_days
        Plants.count += 1

    def display_info(self) -> None:
        """Displays info about the created plant/instance"""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def total_plants() -> None:
        """Displays total created plants/insances from this class"""
        print(f"\nTotal plants created: {Plants.count}")


rose = Plants("Rose", 25, 30)
oak = Plants("Oak", 200, 365)
cactus = Plants("Cactus", 5, 90)
sun_flower = Plants("Sunflower", 80, 45)
fern = Plants("Fern", 15, 120)


print("=== Plant Factory Output ===")
rose.display_info()
oak.display_info()
cactus.display_info()
sun_flower.display_info()
fern.display_info()
Plants.total_plants()
