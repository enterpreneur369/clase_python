"""Class for Car model"""
from clase_python.core.abcs.vehicle import Vehicle

MAX_DISTANCE_TRAVELED = 5

AVAILABLE_CAR_BRANDS = ["NISSAN", "BMW", "MAZDA"]

class Car(Vehicle):

    def __init__(self, brand: str, model: int, door_quantity: int) ->None:
        """Constructor for Car class"""
        self.__brand = brand
        self.__model = model
        self.__door_quantity = door_quantity
        self.__distance_traveled = 0
        self.running = False

    def move(self, aditional_distance: int) -> None:
        if aditional_distance < 0:
            aditional_distance = 0
        if aditional_distance <= MAX_DISTANCE_TRAVELED:
            self.distance_traveled += aditional_distance
        else:
            self.distance_traveled += MAX_DISTANCE_TRAVELED

    def run(self):
        self.running = True
        print("Running...")

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        if brand in AVAILABLE_CAR_BRANDS:
            self.__brand = brand
        else:
            print("No es una marca válida")

    @property
    def distance_traveled(self):
        return self.__distance_traveled
    
    @distance_traveled.setter
    def distance_traveled(self, distance_traveled):
        self.__distance_traveled = distance_traveled