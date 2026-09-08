import vehicle

class PushBike(vehicle.Vehicle):
    def __init__(self):
        """
        Setting up a push-bike that is much slower than cars
        """
        super().__init__()
        self.name = "Push Bike"
        self._acceleration = 1
        self._deceleration = 5
        self._max_speed = 20

