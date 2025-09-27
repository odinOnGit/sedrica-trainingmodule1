class Car:
  def __init__(self, make: str, model: str, price: float):
    self.make: str = make
    self.model: str = model
    self.price: float = price

  def discount(self, percentage: float) -> None:
    if percentage < 0 or percentage > 100:
      raise ValueError("Discount must be below 0 and 100")
    else:
      discount_amount = self.price * (percentage / 100)
      self.price -= discount_amount


  def get_info(self)->str:
    return f"Car:{self.make}, Model: {self.model}, Price: ${self.price:,.2f}"
  

my_car = Car(make="Toyota", model="Corolla", price=25000.0)

# Car info before discount
print("Initial Car Infos")
print(my_car.get_info())

# Discount
my_car.discount(10)
print(my_car.get_info())