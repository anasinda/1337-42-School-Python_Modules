class SecurePlant:
    def __init__(self, name: str, height_cm: int, age_days: int):
        """Set up plant attributes"""
        self.name = name
        self._height = height_cm
        self._age = age_days

    def get_name(self) -> None:
        """Gets the name attribute of the instance"""
        return self.name

    def get_height(self) -> int:
        """Gets the height attribute of the instance"""
        return self._height

    def get_age(self) -> int:
        """Gets the age attribute of the instance"""
        return self._age

    def set_height(self, new_height: int) -> None:
        """Set height if conditions match"""
        if new_height < 0:
            print(f"\nInvalid operation attempted: height {new_height}cm "
                  "[REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        """Set age if conditions match"""
        if new_age < 0:
            print(f"\nInvalid operation attempted: age {new_age} days "
                  "[REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days [OK]")

    def get_info(self) -> None:
        """Get details about plant"""
        print(f"Current plant: {self.name} ({self.get_height()}cm, "
              f"{self.get_age()} days)")


rose = SecurePlant("Rose", 1, 1)

print("=== Garden Security System ===")
print(f"Plant created: {rose.get_name()}")
rose.get_name()
rose.set_height(25)
rose.set_age(30)
rose.set_height(-5)
rose.get_info()
