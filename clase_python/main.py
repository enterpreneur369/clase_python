from model.car import Car

def main():
    print("=.0")
    carro1: Car = Car("NIssan", 2023, 4)
    carro1.move(4)
    print(carro1.distance_traveled)


if __name__ == "__main__":
    main()