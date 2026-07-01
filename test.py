import time
from car import Car, EV, CO2

def main():
    car = CO2()

    while True:
        car.update()
        time.sleep(0.05)  # 20 Hz polling rate

if __name__ == "__main__":
    main()