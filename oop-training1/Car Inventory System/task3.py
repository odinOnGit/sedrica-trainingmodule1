class Car:
  def __init__(self, make: str, model: str, price: float):
    self.make: str = make
    self.model: str = model
    self.price: float = price

  def get_info(self) -> str:
    return f"Car: {self.make}, Model: {self.model}, Price: ${self.price:,.2f}"

  
class ElectricCar(Car):
  def __init__(self, make: str, model: str, price: float, battery_range: float):
    super().__init__(make, model, price)
    self.battery_range: float = battery_range

  def get_info(self) -> str:
    base_info = super().get_info()
    return f"{base_info}, Battery Range: {self.battery_range} miles"


class SportsCar(Car):
  def __init__(self,make: str, model: str, price: float, top_speed: float):
    super().__init__(make, model, price)
    self.top_speed: float = top_speed

  def get_info(self) -> str:
    base_info = super().get_info()
    return f"{base_info}, Top Speed: {self.top_speed}"
  


my_car = Car(make="Ford", model="Mustang", price=45000.0)

elec_car = ElectricCar(make = "Tesla", model="Model S",price = 79999.0, battery_range=396)
sports_car = SportsCar(make = "Porshe", model = "911", price = 114400.0, top_speed=191)

print(my_car.get_info())
print(elec_car.get_info())
print(sports_car.get_info())