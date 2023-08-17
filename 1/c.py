from enum import Enum


animal_sounds = {
  'cat': 'meow',
  'dog': 'woouf'
}

class Animal1:
  def __init__(self, animal_type) -> None:
    self.animal_type = animal_type

  def make_sound(self):
    if self.animal_type in animal_sounds.keys():
      print(animal_sounds[self.animal_type])
    else:
      print("Нету накого животного")











class AnimalSounds(Enum):
  cat = 'meow'
  dog = 'woouf'


class Animal:
  def __init__(self, animal_type) -> None:
    self.animal_type = animal_type

  def make_sound(self):
    print(self.animal_type)


a = Animal(AnimalSounds.dog.value)
a.make_sound()


