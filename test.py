import time
from car import Car, EV, CO2

def main():
    car = EV()

    try:
        while True:
            car.update()
            time.sleep(0.05)
    except KeyboardInterrupt:
        car.stop_motors()
        print("Shutting down.")

if __name__ == "__main__":
    main()