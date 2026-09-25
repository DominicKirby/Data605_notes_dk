import vehicle

class FastCar(vehicle.Vehicle):
    def __init__(self):
        """
        Setting up a quicker car with higher top speed
        """
        super().__init__()
        self.name = "Fast Car"
        self._acceleration = 5
        self._deceleration = 10
        self._max_speed = 150


