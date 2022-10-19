#super()

class User():
  def __init__(self,email):
    self.email=email
    print()
  def login():
    print("you are logged in ")
  def attack(self):
    print("Do nothing")
class Wizard(User):
  def __init__(self,name,power,email):
    super().__init__(email)                    
    self.name=name
    self.power=power
  def attack(self):
    User.attack(self)
    print(f"attacking with the power of {self.name}")

class Archer():
  def __init__(self, name,arrows):
    self.name=name
    self.arrows=arrows
  def attack(self):
    print(f'attacking with the arrows {self.arrows}')
wizard1=Wizard("aman",100,"aman@gmail.com")
archer1=Archer("prince",50)
print(wizard1.email)
print(dir(wizard1))#gives all methods list which we can use on this wizard1
