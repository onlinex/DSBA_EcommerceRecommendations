class Cake:
  p = 0

  @classmethod
  def change(cls):
    cls.p = cls.p + 1
  
  def __init__(self):
    Cake.p = Cake.p + 1
  
c1 = Cake() #Object1
print('Accessing class variable using object c1: ', c1.p)
print('Accessing class variable using classname: ', Cake.p)

c1.change()
print('Accessing class variable using object c1: ', c1.p)
print('Accessing class variable using classname: ', Cake.p)

c2 = Cake()  #Object2
print('Accessing class variable using object c1: ', c1.p)
print('Accessing class variable using object c2: ', c2.p)
print('Accessing class variable using classname: ', Cake.p)