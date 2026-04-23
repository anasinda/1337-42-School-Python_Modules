class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int):
        """Setting up plant attributes"""
        self.name = name
        self.height = height_cm
        self.age = age_days

    def get_stats(self) -> None:
        """Get info about plant."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)
sun_flower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
rose.get_stats()
sun_flower.get_stats()
cactus.get_stats()
