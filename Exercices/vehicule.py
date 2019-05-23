from dataclasses import dataclass
from abc import ABCMeta, abstractmethod

@dataclass
class Data_vehicule:
    miles : int
    make  : int  
    model : str
    year  : int
    sold_on : bool


class Vehicle(metaclass=ABCMeta):
    """A car for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the car has.
        miles: The integral number of miles driven on the car.
        make: The make of the car as a string.
        model: The model of the car as a string.
        year: The integral year the car was built.
        sold_on: The date the vehicle was sold.
    """
    __metaclass__ = ABCMeta
    base_sale_price = 0
    wheels = 0

    def __init__(self, data_cls):
        self._data_cls = data_cls
 

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self._data_cls.__dict__["sold_on"] is True:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self._data_cls.__dict__["sold_on"] is False:
            return 0.0  # Not yet sold
        return self._data_cls["base_sale_price"] - (.10 * self._data_cls["miles"])

    @abstractmethod
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass
    def __str__(self):
        return "type >" + "  " + "< modele >" + self._data_cls.__dict__["model"] + "< annee >" + self._data_cls["year"] + "<"

class Car(Vehicle):
    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        return "car"

class Truck(Vehicle):
    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        return "truck"

class Moto(Vehicle):
    pass

if __name__ == "__main__":
    vehicule1 = Car(Data_vehicule(10000,2015,"model1",1995,False))
    print("Vehicule1 de type ",vehicule1)
    print("Vehicule1 de type ",vehicule1.vehicle_type())
    print("Prix de vente vehicule1 : ", vehicule1.sale_price())
    print("==============")
    print("")
    vehicule2 = Truck(Data_vehicule(100000,2015,"model1",1995,False))
    print("Vehicule1 de type ",vehicule2.vehicle_type())

    #vehicule3 = Moto(Data_vehicule(100000,2015,"model1",1995,False))
    #print("Vehicule1 de type ",vehicule2.vehicle_type())
