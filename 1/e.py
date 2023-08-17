def Teacher(name):
  name = name

  def print_name():
    print(name)
  
  def get_name():
    return name

  def set_name(new_name):
    name = new_name

  return (print_name, get_name, set_name)



pr, g, s = Teacher('Nurzhan')
pr()
s('nurzhan')
pr()