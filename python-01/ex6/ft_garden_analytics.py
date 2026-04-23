class Plant:

    def __init__(self, name: str, height_cm: int):
        """Setting up plant attributes"""
        self.name = name
        self.height = height_cm
        self.growth = 0

    def grow(self, growth_len: int = 1):
        """Grows plant by len of attribute"""
        self.height += growth_len
        self.growth += growth_len
        return f"{self.name} grew {growth_len}cm"

    def get_info(self):
        """Get details about plant"""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height_cm: int, flower_color):
        """Setting up flower attributes"""
        super().__init__(name, height_cm)
        """Inherit attributes from parent class"""
        self.color = flower_color
        self.bloom_state = False

    def bloom(self):
        """Set bloom state to true"""
        self.bloom_state = True

    def get_info(self):
        """Get details about flower that it inherited from parent +
        its own specialized details"""
        """Check bloom state and return depending on what we get"""
        status = "blooming" if self.bloom_state else "not blooming"
        return f"{super().get_info()}, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height_cm: int, flower_color: str,
                 prize_points: int):
        """Setting up prize flower attributes"""
        super().__init__(name, height_cm, flower_color)
        """Inherit attributes from parent class"""
        self.prize_points = prize_points

    def get_info(self):
        """Get details about flower that it inherited from parent +
        its own specialized details"""
        return f"{super().get_info()}, Prize points: {self.prize_points}"


class GardenManager:
    total_gardens = 0

    def __init__(self, manager):
        """Setting up instance attribute"""
        self.manager = manager
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plants(self, plant: Plant):
        """Adding instances of plant class and it's children to list"""
        self.plants.append(plant)
        return (f"Added {plant.name} to {self.manager}'s Garden")

    def grow_all(self, sign):
        """Growing plants method"""
        if sign == 0:
            print(f"{self.manager} is helping all plants grow...")
        for plant in self.plants:
            if sign == 0:
                print(plant.grow())
            else:
                plant.grow()

    def bloom_all(self):
        """Bloom plants depending on class method"""
        for plant in self.plants:
            if isinstance(plant, FloweringPlant | PrizeFlower):
                plant.bloom()

    def manager_report(self):
        """Prints which plants each manager has"""
        print(f"==={self.manager}'s Garden Report")
        print("Plants in garden:")
        for plant in self.plants:
            print("-", plant.get_info())

    @classmethod
    def create_garden_network(cls):
        """Creates a list of garden manager instances"""
        return [cls("Alice"), cls("Bob")]

    class GardenStats:

        @staticmethod
        def total_gp(plants: list):
            """Prints number of plants and their total growth per manager"""
            amount = 0
            total_plants = 0
            for plant in plants:
                amount += plant.growth
                total_plants += 1
            print(f"Plants added: {total_plants}, Total growth: {amount}cm")

        @staticmethod
        def type_count(plants: list):
            """Returns each type of plant we have in our list"""
            stats_dic = {"plant": 0, "flowering": 0, "prize": 0}
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    stats_dic["prize"] += 1
                elif isinstance(plant, FloweringPlant):
                    stats_dic["flowering"] += 1
                else:
                    stats_dic["plant"] += 1
            print(f"Plant types: {stats_dic['plant']} regular, "
                  f"{stats_dic['flowering']} flowering, "
                  f"{stats_dic['prize']}, prize flowers")

        @staticmethod
        def height_val(plants: list, sign):
            """Validates height of each plant"""
            validation = False
            score = 0
            for plant in plants:
                if plant.height > 0:
                    validation = True
                    score += 10
                else:
                    validation = False
            if sign == 0:
                print(f"Height validation test: {validation}")
            return score

        @staticmethod
        def get_gs(plants: list, score: int):
            """Gets garden score combining height + prize score"""
            total = 0
            for plant in plants:
                total += plant.height
                if isinstance(plant, PrizeFlower):
                    total += plant.prize_points
            return total + score

        @staticmethod
        def get_total_gardens():
            """Prints total gardens managed"""
            print(f"Total gardens managed: {GardenManager.total_gardens}")


managers = GardenManager.create_garden_network()

apple_tree = Plant("Apple Tree", 10)
daisy = FloweringPlant("Daisy", 15, "white")
oleander = PrizeFlower("Oleander", 24, "pink", 10)

managers[1].add_plants(apple_tree)
managers[1].add_plants(daisy)
managers[1].add_plants(oleander)
managers[1].grow_all(1)
score = managers[0].GardenStats.height_val(managers[1].plants, 1)
garden_score = managers[0].GardenStats.get_gs(managers[1].plants, score)


oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

print("=== Garden Management System Demo ===\n")
print(managers[0].add_plants(oak))
print(managers[0].add_plants(rose))
print(managers[0].add_plants(sunflower))
print("")
managers[0].grow_all(0)
managers[0].bloom_all()
print("")
managers[0].manager_report()
print("")
managers[0].GardenStats.total_gp(managers[0].plants)
managers[0].GardenStats.type_count(managers[0].plants)
print("")
score = managers[0].GardenStats.height_val(managers[0].plants, 0)
garden_score2 = managers[0].GardenStats.get_gs(managers[0].plants, score)
print(f"Garden scores - {managers[0].manager}: "
      f"{garden_score2}, {managers[1].manager}: {garden_score}")
managers[0].GardenStats.get_total_gardens()
