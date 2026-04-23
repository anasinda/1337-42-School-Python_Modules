class Plant:
    def __init__(
            self, name: str, plant_type: str, height_cm: int, age_days: int):
        """Setting up plant attributes"""
        self.name = name
        self.type = plant_type
        self.height = height_cm
        self.age = age_days

    def get_info(self) -> str:
        """Get details about plant"""
        return f"{self.name} ({self.type}): {self.height}cm, {self.age} days, "


class Flower(Plant):
    def __init__(
            self, name: str, plant_type: str, height_cm: int, age_days: int,
            flower_color: str):
        """Set up flower attributes"""
        super().__init__(name, plant_type, height_cm, age_days)
        """Inherit attributes from parent class"""
        self.color = flower_color

    def bloom(self) -> None:
        """Sets up the bloom attribute for this instance and prints it"""
        bloom: str = f"{self.name} is blooming beautifully!"
        print(bloom)

    def get_more_info(self) -> None:
        """Get details about flower that it inherited from parent +
        its own specialized details"""
        info: str = f"{super().get_info()}{self.color} color"
        print(info)


class Tree(Plant):
    def __init__(
            self, name: str, plant_type: str, height_cm: int, age_days: int,
            trunk_diameter: int):
        """Set up tree attributes"""
        super().__init__(name, plant_type, height_cm, age_days)
        """Inherit attributes from parent class"""
        self.diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculates shade of tree depending on its diameter"""
        res: int = (3.14 * ((self.height / 100) ** 2))
        shade: str = f"{self.name} provides {res:.0f} square meters of shade"
        print(shade)

    def get_more_info(self) -> None:
        """Get details about tree that it inherited from parent +
        its own specialized details"""
        info: str = f"{super().get_info()}{self.diameter}cm diameter"
        print(info)


class Vegetable(Plant):
    def __init__(
            self, name: str, plant_type: str, height_cm: int, age_days: int,
            harvest_season: str, nut_value: str):
        """Set up vegetable attributes"""
        super().__init__(name, plant_type, height_cm, age_days)
        """Inherit attributes from parent class"""
        self.season = harvest_season
        self.value = nut_value

    def nutritional_value(self) -> None:
        """Gets what what nutritional value the tree provides"""
        n_v = f"{self.name} is rich in {self.value}"
        print(n_v)

    def get_more_info(self) -> None:
        """Get details about vegetable that it inherited from parent +
        its own specialized details"""
        info = f"{super().get_info()}{self.season}"
        print(info)


print("=== Garden Plant Types ==\n")
rose = Flower("Rose", "Flower", 25, 30, "red")
rose.get_more_info()
rose.bloom()
print("\n")
oak = Tree("Oak", "Tree", 500, 1825, 50)
oak.get_more_info()
oak.produce_shade()
print("\n")
tomato = Vegetable(
    "Tomato", "Vegetable", 80, 90, "summer harvest", "vitamin C")
tomato.get_more_info()
tomato.nutritional_value()
