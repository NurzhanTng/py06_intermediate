class Car:
  def __init__(self, mark, color) -> None:
    self.mark = mark
    self.color = color

  def __str__(self) -> str:
    return f"class Car\n  self.mark: {self.mark}\n  self.color: {self.color}\n"

  def get_info(self) -> str:
    print(f"Марка вашей машины {self.mark}")



c1 = Car('Toyota', 'white')

# print(c1, c1, c1)
c1.get_info()