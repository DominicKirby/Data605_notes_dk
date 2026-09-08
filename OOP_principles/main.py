import fastcar
import slowcar
import pushbike

print("=" * 31)
print("Fast Car acceleration and deceleration tests.")
print("=" * 31)

fast_car = fastcar.FastCar()

print("-- Acceleration --\n") #

fast_car.accelerate(0.5, 4)
print(f'Accelerating at 50% for 4 seconds to a current speed of {fast_car.current_speed()}')

fast_car.accelerate(1, 100)
print(f'Accelerating 100% for 100 seconds to a current speed of {fast_car.current_speed()}')

print("\n-- Deceleration --\n")

fast_car.decelerate(0.5, 6)
print(f'Decelerating at 50% for 6 seconds to a current speed of {fast_car.current_speed()}')

fast_car.decelerate(1, 100)
print(f'Decelerating at 100% for 100 seconds to current speed of {fast_car.current_speed()}')

print("=" * 31)
print("Slow Car acceleration and deceleration tests.")
print("=" * 31)

slow_car = slowcar.SlowCar()

print("-- Acceleration --\n")

slow_car.accelerate(0.5, 4)
print(f'Accelerating at 50% for 4 seconds to a current speed of {slow_car.current_speed()}')

slow_car.accelerate(1, 100)
print(f'Accelerating 100% for 100 seconds to a current speed of {slow_car.current_speed()}')

print("\n-- Deceleration --\n")

slow_car.decelerate(0.5, 6)
print(f'Decelerating at 50% for 6 seconds to a current speed of {slow_car.current_speed()}')

slow_car.decelerate(1, 100)
print(f'Decelerating at 100% for 100 seconds to a current speed of {slow_car.current_speed()}')

print("=" * 31)
print("Push Bike acceleration and deceleration tests.")
print("=" * 31)

push_bike = pushbike.PushBike()

print("-- Acceleration --\n")

push_bike.accelerate(0.5, 4)
print(f'Accelerating at 50% for 4 seconds to a current speed of {push_bike.current_speed()}')

push_bike.accelerate(1, 100)
print(f'Accelerating at 100% for 100 seconds to a current speed of {push_bike.current_speed()}')

print("\n-- Deceleration --\n")

push_bike.decelerate(0.5, 6)
print(f'Decelerating at 50% for 6 seconds to a current speed of {push_bike.current_speed()}')

push_bike.decelerate(1, 100)
print(f'Decelerating at 100% for 100 seconds to a current speed of {push_bike.current_speed()}')

print("=" * 31)