import vehicle

class SlowCar(vehicle.Vehicle):
    def __init__(self):
        """
        Setting up a slow car with lower acceleration and top speed
        """
        super().__init__()
        self.name = "Slow Car"
        self._acceleration = 3
        self._deceleration = 10
        self._max_speed = 125