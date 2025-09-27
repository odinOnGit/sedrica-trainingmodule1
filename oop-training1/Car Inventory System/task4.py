class Car:
  def __init__(self, make: str, model: str, price: float):
    self.make = make
    self.model = model
    self.__price = price

  def get_info(self) -> str:
    return f"Car: {self.make}, Model: {self.model}, Price: {self.__price:,.2f}"
  

class ElectricCar(Car):
  def __init__(self, make: str, model: str, price: float, battery_range: float):
    super().__init__(make, model, price)
    self.battery_range = battery_range

  def get_info(self):
    temp = super().get_info()
    return f"{temp}, Battery Range: {self.battery_range} miles"

class SportsCar(Car):
  def __init__(self, make: str, model: str, price: float, top_speed: float):
    super().__init__(make, model, price)
    self.top_speed = top_speed

  def get_info(self):
    temp = super().get_info()
    return f"{temp}, Top Speed: {self.top_speed} miles/hr"
  
cars = [
  {
    "make": "Ford",
    "model": "Mustang",
    "price": 45000.0,
    "battery_range": 380,
    "top_speed": 190
  },
  {
    "make": "Toyota",
    "model": "Corolla",
    "price": 30000.0,
    "battery_range": 395,
    "top_speed": 165
  }
]

#for car in cars:
 # my_gen_car = Car(make = car['make'], model = car['model'], price = car['price'])
  #temp2 = my_gen_car.get_info()
 # print(temp2)

#for car in cars:
 # my_electric_car = ElectricCar(make = car['make'], model=car['model'], price=car['price'], battery_range=car['battery_range'])
 # temp2 = my_electric_car.get_info()
 # print(temp2)

#for car in cars:
  #my_sports_car = SportsCar(make = car['make'], model=car['model'], price=car['price'], top_speed=car['top_speed'])
  #temp2 = my_sports_car.get_info()
  #print(temp2)


# quite not, so

my_garage = [
  Car("Toyota", "Corolla", 25000.0),
  ElectricCar("Tesla", "Model 3", 45000.0, 390),
  SportsCar("Porshe", "911", 1442200.0, 191)
]

for vehicle in my_garage:
  print(vehicle.get_info())