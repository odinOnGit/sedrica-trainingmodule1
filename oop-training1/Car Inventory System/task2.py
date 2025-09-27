class Car:
  def __init__(self, make: str, model: str, price:float):
    self.make: str = make
    self.model: str = model
    self.__price: float = price if price >= 0 else 0.0

  def get_price(self) -> float:
    return self.__price
  
  def set_price(self, new_price: float) -> None:
    if new_price < 0:
      print("Error: We're price takers")

    else:
      self.__price = new_price

  def apply_discount(self, percentage: float) -> None:
    if not 0 < percentage < 100:
      raise ValueError("Error: Cannot give a discount on discount. Please check on percentage")
    else:
      discount_amount = self.__price * (percentage / 100)
      self.__price -= discount_amount

  def get_info(self) -> str:
    return f"Car: {self.make}, Model: {self.model}, Price: ${self.__price:,.2f}"
  
  
if __name__ == "__main__":
  my_dream_car = Car(make="Ford", model="Mustang", price=45000.0)
  print("__Initial Info__")
  print(my_dream_car.get_info())

  print(f"\nGetting price with getter: ${my_dream_car.get_price():,.2f}")

  print("Setting price to $42000 using setter...")
  my_dream_car.set_price(42000.0)
  print(my_dream_car.get_info())

  # checking if price is private
  try:
    print(my_dream_car.__price)
  except AttributeError as e:
    print(f"\nCannot access private attributes directly: {e}")