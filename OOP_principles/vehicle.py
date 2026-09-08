class Vehicle:
    # Attributes
    def __init__(self):
        """
        Default setup for all vehicles
        """
        self.name = "Vehicle"
        self._acceleration = 1
        self._deceleration = 1
        self._current_speed = 0
        self._max_speed = 150


    def accelerate(self, percentage, time):
        """
        Acceleration based on percentage of acceleration and time accelerated, for up to the maximum speed
        """
        if percentage < 0 or percentage > 1: # Percentages edge cases
            return "percentage acceleration must be between 0 and 1."

        if self._current_speed + self._acceleration * percentage * time < self._max_speed: # To ensure speed is not above maximum
            self._current_speed += self._acceleration * percentage * time
        else: # Else set to the max speed
            self._current_speed = self._max_speed

        return None

    def decelerate(self, percentage, time):
        """
        Deceleration based on percentage of braking and time braking, for anything above 0
        """
        if percentage < 0 or percentage > 1: # Percentages edge cases
            return "percentage deceleration must be between 0 and 1."

        if self._current_speed - self._deceleration * percentage * time > 0: # Ensure speed stays above 0
            self._current_speed -= self._deceleration * percentage * time
        else: # Else set the speed to 0
            self._current_speed = 0

        return None

    def current_speed(self): # Getter
        """
        Getter function to call upon the current speed on the vehicle
        """
        return self._current_speed